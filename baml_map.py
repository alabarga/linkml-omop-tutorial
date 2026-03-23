#!/usr/bin/env python3
"""
Tutorial CLI: BAML structured output (``MapOmopTable``) → linkml-map YAML.

Same flow as ``llm_map.py`` (digests, CDM CSV help, validation), but the mapping
step uses the generated client in ``syntactic/baml_client`` (OpenAI only).

Requires ``baml-py`` matching ``syntactic/baml_src/generators.baml`` version.
Regenerate with::

  cd syntactic && baml-cli generate

Environment (see also ``syntactic/config.py``):

- ``OPENAI_API_KEY`` (required)
- ``OPENAI_MODEL`` — optional here if you pass ``--model`` (sets env for the run)
- ``OPENAI_BASE_URL`` — optional; set explicitly for OpenAI-compatible gateways
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

import yaml
from linkml_runtime.utils.schemaview import SchemaView

_ROOT = Path(__file__).resolve().parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from agents.omop_targets import iter_omop_class_names  # noqa: E402
from agents.pipeline import load_dotenv_for_repo  # noqa: E402
from agents.validate import (  # noqa: E402
    local_dry_run_validation,
    validate_map_yaml_string,
)
from agents.map_normalize import normalize_map_shape  # noqa: E402
from agents.omop_cdm_help import (  # noqa: E402
    default_help_dir,
    format_table_help,
    load_field_help_text,
    load_table_row,
)
from llm_map import (  # noqa: E402
    _candidate_source_classes,
    _digest_class,
    _infer_source_class,
    _openai_model,
    _required_target_slots,
    _sample_rows,
)
from syntactic.utils import map_omop_table_sync  # noqa: E402


def baml_spec_to_map_dict(
    spec: Any,
    *,
    target_class: str,
    source_class: str,
) -> dict[str, Any]:
    """Convert BAML ``LinkmlMapSpec`` (slot_rules) to linkml-map YAML dict."""
    prefixes = {
        "linkml": "https://w3id.org/linkml/",
        "omop_cdm": "https://w3id.org/omop_cdm",
    }
    out: dict[str, Any] = {"prefixes": prefixes}
    slot_derivations: dict[str, Any] = {}
    for rule in spec.slot_rules:
        cell: dict[str, Any] = {}
        pf = getattr(rule, "populated_from", None)
        ex = getattr(rule, "expr", None)
        if pf is not None and ex is not None:
            raise ValueError(
                f"Slot {rule.target_slot!r}: use either populated_from or expr, not both"
            )
        if pf is not None:
            cell["populated_from"] = pf
        if ex is not None:
            cell["expr"] = ex
        if not cell:
            raise ValueError(f"Slot {rule.target_slot!r} needs populated_from or expr")
        slot_derivations[rule.target_slot] = cell
    out["class_derivations"] = {
        target_class: {
            "populated_from": source_class,
            "slot_derivations": slot_derivations,
        }
    }
    return out


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True, type=Path, help="Source LinkML schema YAML")
    p.add_argument("--target", required=True, type=Path, help="Target LinkML schema YAML")
    p.add_argument(
        "--source-class",
        default=None,
        help="Source LinkML class. If omitted, inferred via PydanticAI (same as llm_map.py).",
    )
    p.add_argument(
        "--target-class",
        default=None,
        help="Target OMOP class, e.g. person. Omit when using --all-omop-classes.",
    )
    p.add_argument("--sample", required=True, type=Path, help="Sample CSV for dry-run validation")
    p.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output map YAML path (required unless --all-omop-classes)",
    )
    p.add_argument(
        "--all-omop-classes",
        action="store_true",
        help=(
            "Write one map per class in --target schema (same source/sample each time; "
            "demo-oriented — validate each output)."
        ),
    )
    p.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for maps when using --all-omop-classes (default: cwd)",
    )
    p.add_argument("--model", default="gpt-4o-mini", help="Sets OPENAI_MODEL for this process")
    p.add_argument(
        "--api-base",
        default="https://api.openai.com/v1",
        help="Sets OPENAI_BASE_URL for this process",
    )
    p.add_argument("--max-retries", type=int, default=3, help="Attempts after validation failure")
    p.add_argument(
        "--max-target-slots",
        type=int,
        default=None,
        help="Limit target attributes in digest (default: all)",
    )
    p.add_argument("--dry-run", action="store_true", help="Print digests only; no API")
    p.add_argument(
        "--skip-validation",
        action="store_true",
        help="Write LLM output without linkml-map dry-run (not recommended)",
    )
    help_dir = default_help_dir(_ROOT)
    p.add_argument(
        "--cdm-table-csv",
        type=Path,
        default=help_dir / "OMOP_CDMv5.4_Table_Level.csv",
    )
    p.add_argument(
        "--cdm-field-csv",
        type=Path,
        default=help_dir / "OMOP_CDMv5.4_Field_Level.csv",
    )
    return p.parse_args(argv)


def _run_one_target(
    *,
    args: argparse.Namespace,
    src_sv: SchemaView,
    tgt_sv: SchemaView,
    source_class: str,
    target_class: str,
    sample_yaml: str,
    out_path: Path,
) -> None:
    table_row = load_table_row(target_class, args.cdm_table_csv)
    cdm_table_help = format_table_help(table_row)
    cdm_field_help = load_field_help_text(target_class, args.cdm_field_csv)
    required = _required_target_slots(args.target.resolve(), target_class)
    source_digest = _digest_class(src_sv, source_class, max_slots=None)
    target_digest = _digest_class(
        tgt_sv, target_class, max_slots=args.max_target_slots
    )

    if args.dry_run:
        print(f"=== {target_class} ===\n")
        print(source_digest[:4000])
        print(target_digest[:4000])
        return

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required (repo .env or environment).")

    last_err: str | None = None
    map_dict: dict[str, Any] | None = None

    for attempt in range(1, args.max_retries + 1):
        required_msg = required
        if last_err is not None:
            required_msg = (
                f"{required}\n\n### Fix previous validation error\n{last_err}"
            )

        spec = map_omop_table_sync(
            source_class=source_class,
            target_class=target_class,
            source_digest=source_digest,
            target_digest=target_digest,
            cdm_table_help=cdm_table_help,
            cdm_field_help=cdm_field_help,
            required_target_slots=required_msg,
            sample_csv_yaml=sample_yaml,
        )
        raw = baml_spec_to_map_dict(
            spec, target_class=target_class, source_class=source_class
        )
        raw = normalize_map_shape(raw)
        yaml_text = yaml.safe_dump(raw, sort_keys=False, allow_unicode=True)

        if args.skip_validation:
            map_dict = raw
            break
        try:
            parsed = validate_map_yaml_string(yaml_text, target_class=target_class)
            local_dry_run_validation(
                source_schema_path=args.source.resolve(),
                target_schema_path=args.target.resolve(),
                map_obj=parsed,
                source_type=source_class,
                target_class=target_class,
                sample_csv=args.sample.resolve(),
            )
            map_dict = parsed
            break
        except Exception as exc:  # noqa: BLE001
            last_err = f"{type(exc).__name__}: {exc}"
            if attempt >= args.max_retries:
                raise SystemExit(
                    f"Validation failed after {args.max_retries} attempt(s). Last error:\n{last_err}"
                ) from exc

    assert map_dict is not None
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        yaml.safe_dump(map_dict, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    load_dotenv_for_repo(_ROOT)

    os.environ["OPENAI_MODEL"] = os.environ.get("OPENAI_MODEL") or args.model
    base = args.api_base.rstrip("/")
    if base:
        os.environ["OPENAI_BASE_URL"] = base

    if args.all_omop_classes:
        if args.output is not None:
            raise SystemExit("Do not pass --output with --all-omop-classes (use --output-dir).")
        out_dir = args.output_dir or Path.cwd()
    else:
        if args.target_class is None:
            raise SystemExit("--target-class is required unless --all-omop-classes.")
        if args.output is None:
            raise SystemExit("--output is required unless --all-omop-classes.")

    src_sv = SchemaView(str(args.source.resolve()))
    tgt_sv = SchemaView(str(args.target.resolve()))
    sample_yaml = _sample_rows(args.sample)

    if args.dry_run:
        if args.source_class:
            dry_source = args.source_class
        else:
            cand = _candidate_source_classes(src_sv)
            dry_source = cand[0] if cand else "Patient"
        if args.all_omop_classes:
            for tc in iter_omop_class_names(args.target):
                _run_one_target(
                    args=args,
                    src_sv=src_sv,
                    tgt_sv=tgt_sv,
                    source_class=dry_source,
                    target_class=tc,
                    sample_yaml=sample_yaml,
                    out_path=out_dir / f"{tc}_baml_map.yaml",
                )
            return
        assert args.target_class is not None
        _run_one_target(
            args=args,
            src_sv=src_sv,
            tgt_sv=tgt_sv,
            source_class=dry_source,
            target_class=args.target_class,
            sample_yaml=sample_yaml,
            out_path=args.output or Path("dummy.yaml"),
        )
        return

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is required (repo .env or environment).")

    source_class = args.source_class
    if source_class is None:
        model = _openai_model(args.model, args.api_base, api_key)
        first_target = args.target_class or iter_omop_class_names(args.target)[0]
        table_row = load_table_row(first_target, args.cdm_table_csv)
        cdm_table_blob = format_table_help(table_row)
        source_class = _infer_source_class(
            src_sv=src_sv,
            target_class=first_target,
            sample_csv=args.sample,
            sample_yaml=sample_yaml,
            cdm_table_blob=cdm_table_blob,
            model=model,
            temperature=0.1,
        )
        print(f"Inferred --source-class {source_class!r}", file=sys.stderr)
    elif src_sv.get_class(source_class) is None:
        raise SystemExit(f"Unknown --source-class {source_class!r} in {args.source}")

    if args.all_omop_classes:
        names = iter_omop_class_names(args.target)
        for tc in names:
            out_p = out_dir / f"{tc}_baml_map.yaml"
            try:
                _run_one_target(
                    args=args,
                    src_sv=src_sv,
                    tgt_sv=tgt_sv,
                    source_class=source_class,
                    target_class=tc,
                    sample_yaml=sample_yaml,
                    out_path=out_p,
                )
            except Exception as exc:  # noqa: BLE001
                print(f"Skip {tc}: {exc}", file=sys.stderr)
        return

    assert args.target_class is not None
    assert args.output is not None
    _run_one_target(
        args=args,
        src_sv=src_sv,
        tgt_sv=tgt_sv,
        source_class=source_class,
        target_class=args.target_class,
        sample_yaml=sample_yaml,
        out_path=args.output,
    )


if __name__ == "__main__":
    main()
