# Step 2: Mapping Synthea to OMOP-CDM

> **LLM pipeline:** To auto-generate and validate maps from profiled schemas, follow [LLM_MAP_PIPELINE.md](LLM_MAP_PIPELINE.md) (`profile_synthea_tables.py` → `generate_linkml_map_with_llm.py`). For a minimal single-file flow see **`llm_map.py`** (PydanticAI) or **`baml_map.py`** (BAML / OpenAI).

In this step, we will use `linkml-map` to specify how the source `Patients` data is transformed into the target OMOP-CDM `person` and `death` tables. Generating mapping rules declaratively makes data transformations much easier to maintain, validate, and execute.

## 1. Defining the Mapping Specification

We create a declarative mapping using a YAML file mapping the models. 

Create a file named `models/patients_to_omop_cdm_v54.yaml` and add the following content:

```yaml
prefixes:
  linkml: https://w3id.org/linkml/
  omop_cdm: https://w3id.org/omop_cdm
  MySchema: https://w3id.org/MySchema

enum_derivations:
  GENDER_enum:
    populated_from: GENDER_enum
    mirror_source: true
  RACE_enum:
    populated_from: RACE_enum
    mirror_source: true
  ETHNICITY_enum:
    populated_from: ETHNICITY_enum
    mirror_source: true
  STATE_enum:
    populated_from: STATE_enum
    mirror_source: true
  PREFIX_enum:
    populated_from: PREFIX_enum
    mirror_source: true
  MARITAL_enum:
    populated_from: MARITAL_enum
    mirror_source: true

class_derivations:
  person:
    populated_from: Patients
    slot_derivations:
      person_id:
        expr: "target = abs(hash(src.Id)) % 1000000000"
      person_source_value:
        populated_from: Id
      gender_concept_id:
        expr: "8507 if GENDER == 'M' else (8532 if GENDER == 'F' else 8551)"
      gender_source_value:
        populated_from: GENDER
      year_of_birth:
        expr: "target = int(str(src.BIRTHDATE)[0:4]) if src.BIRTHDATE else None"
      month_of_birth:
        expr: "target = int(str(src.BIRTHDATE)[5:7]) if src.BIRTHDATE else None"
      day_of_birth:
        expr: "target = int(str(src.BIRTHDATE)[8:10]) if src.BIRTHDATE else None"
      birth_datetime:
        populated_from: BIRTHDATE
      race_concept_id:
        expr: "8527 if RACE == 'white' else (8516 if RACE == 'black' else (8515 if RACE == 'asian' else 0))"
      race_source_value:
        populated_from: RACE
      ethnicity_concept_id:
        expr: "38003563 if ETHNICITY == 'hispanic' else 38003564"
      ethnicity_source_value:
        populated_from: ETHNICITY

  death:
    populated_from: Patients
    slot_derivations:
      person_id:
        expr: "target = abs(hash(src.Id)) % 1000000000"
      death_date:
        expr: "target = str(src.DEATHDATE)[0:10] if src.DEATHDATE else None"
      death_datetime:
        populated_from: DEATHDATE
```

### Understanding the Map Configuration
- **`class_derivations`**: Specifies how the target classes are generated from the source class object.
- **`person` & `death`**: Target classes defined in `models/omop_cdm_v54.yaml`.
- **`populated_from`**: The source class (`Patients` inferenced and generated from our `source_schemas/`).
- **`expr`**: Allows evaluation of Python-like expressions. This enables seamless type transformations, string formatting, resolving code mappings like gender to Athena IDs (`8507`, `8532`), and extracting OMOP's `year_of_birth` using subset indexing. Unrestricted execution requires assigning results to `target = ` when running python functions.
- **`enum_derivations`**: LinkML-map requires Enum specifications or mirroring for schema-inferred fields. 

## 2. Environment Setup

Ensure you are using the correct Python environment equipped with LinkML ecosystem libraries:

```bash
source ~/code/environments/linkml-env/bin/activate
```

## 3. Dry-Run Data Mapping Tests

To check that the specification correctly maps attributes, you can process the file using our split mappings via the cli:

```bash
linkml-map map-data -T models/patients_to_person.yaml -s models/patients.yaml --source-type Patients data/patients.csv -o output/person.csv -f csv --unrestricted-eval

# Use awk to stream only patients with a populated DEATHDATE (column 3) to exclude empty rows natively
awk -F',' 'NR==1 || $3 != ""' data/patients.csv > data/dead_patients.csv
linkml-map map-data -T models/patients_to_death.yaml -s models/patients.yaml --source-type Patients data/dead_patients.csv -o output/death.csv -f csv --unrestricted-eval
```

## 4. Evolving Mapping Definitions (v2 & v3)

For maintaining clean logic, we have incrementally refactored `patients_to_person.yaml`. 
- **models/patients_to_person_v2.yaml**: Deprecates Python conditional expressions targeting enum concepts (e.g. `gender_concept_id`) and replaces them entirely with native string-to-integer mappings using the standard LinkML **`value_mappings`** dictionary architecture.
- **models/patients_to_person_v3.yaml**: Takes value matching a step further into the root level. Rather than slot assignments intercepting Enums, the transformation resolves strings directly within `permissible_value_derivations` deployed internally on `enum_derivations`. To ensure the final output retains original string copies safely without getting swept into integers by LinkML, `gender_source_value` actively leverages `expr: target = src.GENDER` to seamlessly bypass the Enum conversion pipeline!

## 5. Advanced Mapping with Datetime Properties Programmatically (v4)

If you attempt mapping property values heavily scoped like `{BIRTHDATE}.year` across CLI data dumps, LinkML will typically issue an `AttributeError` constraint. This originates because the `csv.DictReader` engine automatically parses your data strictly into abstract string dictionaries (`'1992-05-18'`), neglecting your formalized date datatypes.

Instead of writing string slices inline into the CLI maps, we utilize a heavily controlled Python programmatic pipeline in **`scripts/person_v2.py`**. It effectively:
1. Translates the file using proper instantiation into `models.patients.Patients` dataclass objects.
2. Extracts explicitly encapsulated elements like `XSDDateTime` and rehydrates them cleanly backward into valid Python `datetime` instances.
3. Automatically leverages our streamlined **`models/patients_to_person_v4.yaml`** where evaluation logic supports seamless dynamic properties (e.g., `src.BIRTHDATE.year` and `src.BIRTHDATE.month`):

```bash
source ~/code/environments/linkml-env/bin/activate
python scripts/person_v2.py
```
This precisely outputs `output/person_v4.csv` efficiently parsed through strong execution validations!

*In a broader production deployment, pipeline logic typically orchestrates these mappings iteratively over datasets, or models compile mappings directly down to Pandas/Spark transformations via `compile` subcommands.*

## 6. Mapping the Conditions Table

Next, we establish the transformation for `data/conditions.csv` into the OMOP `condition_occurrence` table.

1. **Source Schema**: We natively codify a specific schema (`models/conditions.yaml`) representing the 7 CSV columns (`START`, `STOP`, `PATIENT`, `ENCOUNTER`, `SYSTEM`, `CODE`, `DESCRIPTION`). Because OMOP maps diagnoses specifically via standard vocabulary concepts, we structurally enforce term integrity under the `CODE` attribute by defining a LinkML `reachable_from` constraint referencing the SNOMED-CT tree root natively:
   ```yaml
   enums:
     SnomedCode:
       reachable_from:
         source_ontology: obo:snomed
         source_nodes:
           - snomed:138875005 # SNOMED CT Concept Root
   ```

2. **Mapping Pipeline**: We construct `models/conditions_to_condition_occurrence.yaml` evaluating our `Conditions` concepts securely into OMOP. We explicitly persist the hashing derivation identically mapping UUID strings (`abs(hash(src.PATIENT)) % 1000000000`) assuring complete referential consistency explicitly tracing back securely to the `person_id` previously emitted dynamically in our primary `person` generation.

Since `SnomedCode` validates dynamically against structural Enums, we instruct our configuration to mirror it sequentially to avoid pipeline derivation failures:
```yaml
enum_derivations:
  SnomedCode:
    populated_from: SnomedCode
    mirror_source: true
```

We can execute and validate this standalone component pipeline by streaming the model:
```bash
linkml-map map-data -T models/conditions_to_condition_occurrence.yaml -s models/conditions.yaml --source-type Conditions data/conditions.csv -o output/condition_occurrence.csv -f csv --unrestricted-eval
```


## 7. Agentic Map Generation with LLM + Local Validation

To automate map authoring, we add a lightweight "Model Alignment Agent" script:
`scripts/generate_linkml_map_with_llm.py`.

It follows the same core pattern used by the LinkML Aurelian agent
([reference implementation](https://github.com/monarch-initiative/aurelian/blob/main/src/aurelian/agents/linkml/linkml_agent.py)):
1. Ask an LLM for a LinkML map draft.
2. Validate locally.
3. If validation fails, feed error messages back to the LLM and retry.

### What the Script Does

- Loads source and target LinkML schemas.
- Builds a constrained prompt from:
  - source class slots (for example, `Patients`)
  - target class attributes (for example, `person`)
- Calls an OpenAI-compatible Chat Completions endpoint.
- Parses the YAML proposal.
- Validates structure (`class_derivations`, selected target class).
- Runs a local dry-run mapping with `linkml-map` APIs on a sample CSV row.
- Writes the final map only if validation passes.

### Environment

```bash
source /Users/alabarga/code/environments/linkml-env/bin/activate
export OPENAI_API_KEY="your_api_key_here"
```

### Example: Generate `Patients -> person` Map

```bash
python scripts/generate_linkml_map_with_llm.py \
  --source-schema models/patients.yaml \
  --target-schema models/omop_cdm_v54.yaml \
  --source-type Patients \
  --target-class person \
  --sample-csv data/patients.csv \
  --output-map models/patients_to_person_llm_v8.yaml \
  --model gpt-4o-mini
```

### Execute the Generated Map (linkml-map)

```bash
linkml-map map-data \
  -T models/patients_to_person_llm_v8.yaml \
  -s models/patients.yaml \
  --source-type Patients \
  data/patients.csv \
  -o output/person_llm_v8.csv \
  -f csv \
  --unrestricted-eval
```

### Semantic Validation of `*_concept_id` Values (CONCEPT table)

For OMOP `*_concept_id` fields, we also validate semantic correctness against the local OMOP `CONCEPT.csv.gz` table:

```bash
python scripts/validate_concept_ids.py \
  --input output/person_llm_v8.csv \
  --concept-table vocabularies/CONCEPT.csv.gz
```

This script checks:
- the `concept_id` exists in `CONCEPT.csv.gz`
- the `concept_id` belongs to the expected `domain_id` category (e.g., `Gender` for `gender_concept_id`)
- `concept_id=0` is allowed as an “unknown/not mapped” sentinel
- By default, the script also derives the expected `domain_id` category for each `*_concept_id` column from the OMOP schema `bindings` (so it can be reused beyond just `person`).

### Notes

- The script currently generates one target class per run (`--target-class`), which keeps feedback loops clear and easy to debug.
- For multi-table OMOP outputs (for example `person`, `death`, `condition_occurrence`), run the agent once per target class.
- Local validation remains the source of truth:
  - The agent performs a dry-run mapping using `linkml-map` runtime.
  - It rejects drafts unless required target attributes are populated and have the expected types.
  - Only then does it write the final `linkml-map` YAML.
- The `bindings` you see in the OMOP schema for `*_concept_id` fields serve as “accepted value references”.
- `validate_concept_ids.py` is the step that actually enforces the semantic lookup against `CONCEPT.csv.gz`.
- Schema validation (`linkml-validate`) requires the imported `omop_vocabulary` file.
  - This repo includes a small local stub at `models/omop_vocabulary.yaml` to unblock validation in tutorial mode.

### Optional: Rigorous Schema Validation (linkml-validate)

After generating the map, you can validate the mapped output against `models/omop_cdm_v54.yaml`:

```bash
/Users/alabarga/code/environments/linkml-env/bin/python - <<'PY'
import csv, json, numbers
from pathlib import Path
from linkml_runtime.utils.schemaview import SchemaView
from linkml_map.transformer.object_transformer import ObjectTransformer

sv = SchemaView('models/patients.yaml')
transformer = ObjectTransformer(source_schemaview=sv)
transformer.unrestricted_eval = True
transformer.load_transformer_specification('models/patients_to_person_llm_v8.yaml')

out=[]
with open('data/patients.csv','r',encoding='utf-8') as f:
    reader=csv.DictReader(f)
    for i,row in enumerate(reader):
        if i>=50: break
        mapped = transformer.map_object(row, source_type='Patients')
        # JSON-safe coercion for numpy scalar ints
        for k,v in list(mapped.items()):
            if isinstance(v, (numbers.Integral,)) and not isinstance(v, bool):
                mapped[k] = int(v)
        out.append(mapped)

Path('output/person_llm_v8_list.json').write_text(json.dumps(out), encoding='utf-8')
print('wrote output/person_llm_v8_list.json', len(out))
PY

/Users/alabarga/code/environments/linkml-env/bin/linkml-validate -s models/omop_cdm_v54.yaml -C person output/person_llm_v8_list.json
```