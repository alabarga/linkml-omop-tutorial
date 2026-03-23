# BAML tutorial (Python): `Person` from text

This guide walks you through **creating all BAML sources and generated artifacts** for a minimal example: a **`Person`** type (name, sex, birthdate) and **`ExtractPersonFromText`**, which parses free text into a typed Pydantic model.

Official Python setup: [BAML — Python installation](https://docs.boundaryml.com/guide/installation-language/python).

---

## Prerequisites

1. **Python** with `baml-py` installed (pin the same major.minor as your `baml-cli`):

   ```bash
   pip install baml-py
   ```

   This repo pins a version in `requirements.txt` (e.g. `baml-py==0.220.0`).

2. **`baml-cli`** on your `PATH` (from the same environment as `baml-py`):

   ```bash
   baml-cli --version
   ```

3. **Optional:** [BAML VS Code / Cursor extension](https://marketplace.visualstudio.com/items?itemName=boundary.baml-extension) for syntax highlighting and prompt preview ([docs](https://docs.boundaryml.com/guide/installation-language/python)).

4. **OpenAI** (default client in this tutorial):

   - `OPENAI_API_KEY`
   - `OPENAI_MODEL` (e.g. `gpt-4o-mini`)

---

## Hands-on: create `baml_src` and all artifacts

Follow these steps in order. Paths match this repository’s **`baml_tutorial/`** package; you can use the same layout in your own project (any parent folder name is fine as long as **`baml-cli generate` is run from the directory that contains `baml_src/`** — see Step 4).

### Step 0 — Package layout

From your **project / repo root**, create the tutorial package and the BAML source folder:

```bash
mkdir -p baml_tutorial/baml_src
```

You will add three files under `baml_tutorial/baml_src/`. The **generated** Python client will appear as **`baml_tutorial/baml_client/`** after Step 4 (because `output_dir` in `generators.baml` is `../` relative to `baml_src/`).

**Alternative starter:** Boundary’s `baml-cli init` scaffolds a default `baml_src` (see [install guide](https://docs.boundaryml.com/guide/installation-language/python)). You can run it in an empty folder, then **replace** the generated `.baml` files with the contents below so they match this tutorial.

---

### Step 1 — `generators.baml`

Create **`baml_tutorial/baml_src/generators.baml`**. This declares how the Python client is emitted (`baml_client` next to `baml_src`, Pydantic types, sync client).

> **Version:** set `version` to match your installed `baml-py` / `baml-cli` (run `baml-cli --version`). Mismatches can cause generate or runtime errors.

```baml
generator python_client {
  output_type "python/pydantic"
  output_dir "../"
  version "0.220.0"
  default_client_mode "sync"
}
```

---

### Step 2 — `clients.baml`

Create **`baml_tutorial/baml_src/clients.baml`**. Defines the **OpenAI** LLM client used by functions.

Do **not** add `base_url env.OPENAI_BASE_URL` unless you intend to require that variable everywhere (Boundary treats referenced env vars as mandatory). Omitting `base_url` uses OpenAI’s default API host.

```baml
// OpenAI — OPENAI_API_KEY + OPENAI_MODEL required.

client<llm> OpenAI {
  provider openai
  options {
    model env.OPENAI_MODEL
    api_key env.OPENAI_API_KEY
  }
}
```

---

### Step 3 — `main.baml` (schema + function)

Create **`baml_tutorial/baml_src/main.baml`**:

- **`Person`**: structured output shape (maps to a Pydantic model in Python).
- **`ExtractPersonFromText`**: takes `raw_text`, calls `OpenAI`, returns `Person`. The prompt uses `{{ raw_text }}` interpolation.

```baml
// Tutorial: structured extraction from free text.

class Person {
  name string @description("Full name as stated or best normalized form")
  sex string? @description("e.g. male, female, unknown — use lowercase single word if possible")
  birthdate string? @description("ISO date YYYY-MM-DD if inferable; otherwise null")
}

function ExtractPersonFromText(raw_text: string) -> Person {
  client OpenAI
  prompt #"
    You extract a single person record from unstructured text.

    Rules:
    - If a field is not present or ambiguous, use null (omit or JSON null for optional strings).
    - **name**: required if any person is mentioned; concatenate given + family if split.
    - **sex**: only if explicitly stated or strongly implied by pronouns/titles; else null.
    - **birthdate**: only if a clear calendar date; normalize to YYYY-MM-DD; else null.

    Text to parse:
    ---
    {{ raw_text }}
    ---
  "#
}
```

---

### Step 4 — Generate `baml_client` (first artifact)

Run **`baml-cli generate`** from the directory that **contains** `baml_src/` (not from inside `baml_src/`):

```bash
cd baml_tutorial
baml-cli generate
```

Expected result:

- **`baml_tutorial/baml_client/`** is created or updated (sync client, types, parsers, inlined BAML, etc.).
- You should **not** edit files under `baml_client/` by hand — regenerate after any change to `*.baml`.

**Whenever you edit** `generators.baml`, `clients.baml`, or `main.baml`, run `baml-cli generate` again.

---

### Step 5 — Optional Python wrapper (`__init__.py`)

To import a single helper from your package, add **`baml_tutorial/__init__.py`** at the **same level** as `baml_client/` (sibling of `baml_src/`):

```python
"""BAML tutorial: Person extraction from text."""

from baml_tutorial.baml_client.sync_client import b
from baml_tutorial.baml_client.types import Person

__all__ = ["Person", "b", "extract_person_from_text"]


def extract_person_from_text(raw_text: str) -> Person:
    return b.ExtractPersonFromText(raw_text=raw_text)
```

Imports assume the **repository root** is on `PYTHONPATH` (e.g. run notebooks and scripts from the repo root, or `pip install -e .` if you package the project).

---

### Step 6 — Optional CLI smoke script

This repo includes **`baml_tutorial/run_example.py`**: it loads `.env` from the repo root and calls `extract_person_from_text`. Create it if you want the same behavior:

```bash
python baml_tutorial/run_example.py "Ada Lovelace, 10 December 1815."
```

(See the file in the repo for the full `argparse` + `load_dotenv` implementation.)

---

## Artifact map (after the steps above)

| Path | How it is produced |
|------|---------------------|
| `baml_tutorial/baml_src/generators.baml` | You created (Step 1) |
| `baml_tutorial/baml_src/clients.baml` | You created (Step 2) |
| `baml_tutorial/baml_src/main.baml` | You created (Step 3) |
| `baml_tutorial/baml_client/` | **`baml-cli generate`** (Step 4) |
| `baml_tutorial/__init__.py` | You created (Step 5, optional) |
| `baml_tutorial/run_example.py` | Optional (Step 6) |

---

## Call BAML from Python

From the **repository root** (so `baml_tutorial` is importable):

```python
from baml_tutorial import extract_person_from_text, Person

p = extract_person_from_text(
    "Patient: Maria Chen, DOB 1984-03-22, female, follow-up scheduled."
)
print(p.name, p.sex, p.birthdate)
```

Or use the generated client directly ([Boundary style](https://docs.boundaryml.com/guide/installation-language/python)):

```python
from baml_tutorial.baml_client.sync_client import b

p = b.ExtractPersonFromText(raw_text="Alan Turing, born 23 June 1912.")
```

---

## Jupyter notebooks

Boundary recommends **`%autoreload`** and importing the **`baml_client` package as a module** (e.g. `import baml_tutorial.baml_client as client` then `client.b.ExtractPersonFromText(...)`) so regenerated code reloads without restarting the kernel. See [BAML — Jupyter](https://docs.boundaryml.com/guide/installation-language/python).

### Jupyter kernel vs. shell environment

The notebook kernel often **does not inherit** the same environment variables as your terminal. Load `.env` **inside the notebook** before calling BAML:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path.cwd() / ".env")  # or Path("/absolute/path/to/repo") / ".env"
os.environ.setdefault("OPENAI_MODEL", "gpt-4o-mini")
assert os.environ.get("OPENAI_API_KEY"), "Set OPENAI_API_KEY in .env or the kernel env"
```

---

## Relation to `syntactic/` in this repo

The **OMOP linkml-map** BAML lives under **`syntactic/`** (`MapOmopTable`, etc.). **`baml_tutorial/`** is a smaller, self-contained example for learning the BAML → `baml_client` workflow.

---

## Further reading

- [BAML Python installation](https://docs.boundaryml.com/guide/installation-language/python)
- [What is `baml_client`?](https://docs.boundaryml.com/guide/introduction/baml_client)
- [python-fastapi-starter (examples)](https://github.com/BoundaryML/baml-examples/tree/main/python-fastapi-starter)
