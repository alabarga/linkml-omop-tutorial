# LLM-assisted linkml-map generation (Synthea → OMOP)

This guide describes the pipelines in this repository. There are several ways to drive the **map generator**:

1. **CDM-first (recommended)** — iterate **each OMOP CDM v5.4 table**, let an LLM **choose** the best Synthea source profile, then generate a map. Unknown mappings use **`comments`** for engineers; vocabulary alignment prefers **`enum_derivations`** (not hardcoded `M`/`F` expressions). See **`scripts/generate_omop_maps_from_sources.py`**.
2. **Manual pair** — you already know source + target; call **`scripts/generate_linkml_map_with_llm.py`** once.
3. **Minimal tutorial** — **`llm_map.py`** at the repo root: PydanticAI **structured output** (no agent tools), `SchemaView` digests from your YAML paths, same validation as the script above. Optional: [linkml-pydantic](https://github.com/p2p-ld/linkml-pydantic) packages schemas as importable modules; this CLI reads `.yaml` files directly.
4. **BAML tutorial** — **`baml_map.py`**: same digests, CDM CSV context, and linkml-map validation as `llm_map.py`, but the mapping call is **[Boundary / BAML](https://docs.boundaryml.com/)** (`MapOmopTable` in `syntactic/baml_src/`, generated client under `syntactic/baml_client/`). **OpenAI only** (`OPENAI_API_KEY`, `OPENAI_MODEL`, optional `OPENAI_BASE_URL`). Regenerate the client after editing BAML: `cd syntactic && baml-cli generate` (CLI version should match `baml-py` in `requirements.txt`). For a **minimal** BAML walkthrough (Person + text extract, no OMOP), see **[BAML.md](BAML.md)** and the `baml_tutorial/` package.

Supporting step for both: **`scripts/profile_synthea_tables.py`** — infer LinkML **source** schemas from every CSV under `data/`.

Legacy batch of **fixed** pairs: **`scripts/batch_generate_maps.py`** + `agents/synthea_omop_pairs.yaml` (does not run source selection).

---

## Design principles (CDM-first agent)

- **Target-driven:** prompts are built from `models/omop_cdm_v54.yaml` and [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html) semantics — not from hand-maintained Synthea→OMOP examples.
- **Source selection:** for each OMOP table, a **structured** LLM step picks at most one profiled Synthea table (or **skip** if no plausible source).
- **No assumed source encodings:** do not bake in expressions like `GENDER == 'M'`; real data may use `Male`/`Female`, codes, etc. Prefer **`enum_derivations`** / **`permissible_value_derivations`** when the source schema has enums (see `models/patients_to_person_v4.yaml`).
- **Gaps:** use YAML **`comments`** on `class_derivations` / `slot_derivations` when mapping cannot be derived.

---

## What you get

| Step | Output |
|------|--------|
| Profile | `source_schemas/<csv_stem>_schema.yaml` (plus `raw_<stem>_schema.yaml` intermediates) |
| CDM-first run | `output/omop_maps/<stem>_to_<omop_class>.yaml` and `output/omop_maps/_generation_log.jsonl` |
| Single pair | Path you pass to `--output-map` (e.g. `output/llm_maps/...yaml`) |
| Minimal `llm_map.py` | Path you pass to `--output` (e.g. `patients_to_person_map.yaml`) |
| BAML `baml_map.py` | Same as above; optional `--all-omop-classes` + `--output-dir` for one file per OMOP class |
| Fixed-pair batch | `output/llm_maps/...` from `batch_generate_maps.py` |

Each generated file is **one OMOP target class** per map. Multi-table bundles such as `models/synthea_to_omop_v1.yaml` are **hand-authored or merged** separately; see [MAP.md](MAP.md).

---

## Prerequisites

- **LinkML stack** on your `PATH` inside an activated environment (e.g. `schemauto`, `linkml-map`, `linkml-runtime`):
  ```bash
  schemauto --help
  ```
- **Python dependencies** from the repo root:
  ```bash
  pip install -r requirements.txt
  ```
- **OpenAI-compatible API key** in the repository **`.env`**:
  ```bash
  OPENAI_API_KEY=sk-...
  ```
  Scripts call `load_dotenv_for_repo()` so the key loads from the **project root** `.env` even when the shell cwd is elsewhere.

---

## Step 1 — Profile all Synthea CSVs

From the **repository root**:

```bash
python scripts/profile_synthea_tables.py
```

Defaults: input `data/*.csv`, output `source_schemas/<stem>_schema.yaml`, uses `enrich_schema.py`.

**Class names** come from filenames (e.g. `patients.csv` → `Patients`). More detail: [PROFILE.md](PROFILE.md).

---

## Step 2a — CDM-first: all OMOP tables × best Synthea source (recommended)

Runs profiling unless `--skip-profile` is set. For **each** class in `models/omop_cdm_v54.yaml`:

1. **Selection** LLM: given CDM field context + summaries of all profiled sources (with data files present), choose one `source_schemas/<stem>_schema.yaml` or skip.
2. **Map** LLM: generate and validate a linkml-map for that pair.

```bash
python scripts/generate_omop_maps_from_sources.py
```

Useful flags:

| Flag | Meaning |
|------|--------|
| `--skip-profile` | Do not re-run `profile_synthea_tables.py` |
| `--dry-run` | Print counts only; no API calls |
| `--only-target person` | Repeatable; restrict to specific OMOP class names |
| `--out-dir` | Default `output/omop_maps/` |

Outputs:

- Maps: `output/omop_maps/<stem>_to_<target>.yaml`
- Log: `output/omop_maps/_generation_log.jsonl` (selection + map errors)

**Cost / time:** one selection + one map call per OMOP table (dozens of API calls for a full run). Use `--only-target` while iterating.

---

## Step 2b — Minimal `llm_map.py` (structured output, no tools)

Same validation as the Aurelian-style script (**Step 2c**), but a **single file** and **Pydantic `LinkMLMapSpec`** as the model output (BAML-style prompting, without agent tools). The spec is **slot_rules only** (no LLM-generated `enum_derivations`): mapping enum-like source fields to OMOP integer `*_concept_id` slots must use **`expr`**, or linkml-map raises errors such as `Could not find what to derive from a source GENDER_enum`. For `person`, prompts follow [OMOP CDM v5.4 — person](https://ohdsi.github.io/CommonDataModel/cdm54.html#person).

| Flag | Meaning |
|------|--------|
| `--source` | Source LinkML YAML, e.g. `patients.yaml` |
| `--target` | Target schema, e.g. `models/omop_cdm_v54.yaml` |
| `--source-class` / `--target-class` | LinkML class names, e.g. `Patient` → `person` |
| `--sample` | CSV for one-row dry-run |
| `--output` | Map YAML path |
| `--dry-run` | Print CDM excerpts + prompt preview (no API) |
| `--source-class` | Optional; if omitted, an extra LLM step picks the LinkML class using `help/OMOP_CDMv5.4_Table_Level.csv` + field CSV + schema candidates |
| `--cdm-table-csv` / `--cdm-field-csv` | Override paths to the bundled OHDSI table/field reference exports (default: `help/OMOP_*.csv`) |

```bash
python llm_map.py \
  --source patients.yaml \
  --target models/omop_cdm_v54.yaml \
  --source-class Patient \
  --target-class person \
  --sample data/patients.csv \
  --output patients_to_person_map.yaml
```

Infer source class (e.g. single root class **Patient** still chosen explicitly when multiple classes exist):

```bash
python llm_map.py \
  --source patients.yaml \
  --target models/omop_cdm_v54.yaml \
  --target-class person \
  --sample data/patients.csv \
  --output patients_to_person_map.yaml
```

`condition_occurrence` (and other OMOP tables) use the same flow: `--target-class condition_occurrence` loads the matching rows from the field-level CSV so slot_rules follow that table’s ETL text.

---

## Step 2b-alt — `baml_map.py` (BAML structured output, OpenAI)

Same flags and validation loop as **Step 2b**, except the LLM call is **`syntactic.baml_client`** → `MapOmopTable`. Install **`baml-py`** (pinned in `requirements.txt` to match `generators.baml`).

| Extra flag | Meaning |
|------------|--------|
| `--all-omop-classes` | Emit `{class}_baml_map.yaml` under `--output-dir` for every class in `--target` (same `--sample` each time — use for demos; validate each file). |

```bash
python baml_map.py \
  --source patients.yaml \
  --target models/omop_cdm_v54.yaml \
  --source-class Patient \
  --target-class person \
  --sample data/patients.csv \
  --output patients_to_person_baml_map.yaml
```

---

## Step 2c — Single manual pair (when you already chose source + target)

| Flag | Meaning |
|------|--------|
| `--source-schema` | e.g. `source_schemas/patients_schema.yaml` |
| `--target-schema` | `models/omop_cdm_v54.yaml` |
| `--source-type` | LinkML class name, e.g. `Patients` |
| `--target-class` | OMOP class, e.g. `person` |
| `--sample-csv` | e.g. `data/patients.csv` |
| `--output-map` | Output path |

```bash
python scripts/generate_linkml_map_with_llm.py \
  --source-schema source_schemas/patients_schema.yaml \
  --target-schema models/omop_cdm_v54.yaml \
  --source-type Patients \
  --target-class person \
  --sample-csv data/patients.csv \
  --output-map output/llm_maps/patients_to_person.yaml
```

---

## Step 3 — Fixed-pair batch (legacy)

Pairs in `agents/synthea_omop_pairs.yaml`:

```bash
python scripts/batch_generate_maps.py --dry-run
python scripts/batch_generate_maps.py
```

---

## Running a generated map

```bash
linkml-map map-data \
  -T output/omop_maps/patients_to_person.yaml \
  -s source_schemas/patients_schema.yaml \
  --source-type Patients \
  data/patients.csv \
  -o output/person_from_llm.csv \
  -f csv \
  --unrestricted-eval
```

Validate OMOP-shaped rows:

```bash
linkml-validate -s models/omop_cdm_v54.yaml -C person output/person_from_llm.csv
```

---

## Architecture reference

- **Agent code:** `agents/` — see [agents/AGENT.md](../agents/AGENT.md).
- **CDM context:** `agents/cdm_guidance.py` + `models/omop_cdm_v54.yaml` + [OMOP CDM v5.4](https://ohdsi.github.io/CommonDataModel/cdm54.html) link in prompts.

---

## Troubleshooting

| Issue | What to check |
|-------|----------------|
| `schemauto` not found | Activate the environment where `schema-automator` is installed before profiling. |
| `OPENAI_API_KEY` missing | Repo-root `.env` or export in shell. |
| Map validation fails | `--max-target-attributes`, `--model`, or inspect `comments` in YAML for manual completion. |
| Import errors | Run from repo root; scripts add the root to `sys.path`. |
