#!/bin/bash

# Exit script if any command fails
set -e

# Define directories
DATA_DIR="data"
OUTPUT_DIR="source_schemas"
RAW_SCHEMA="${OUTPUT_DIR}/raw_patients_schema.yaml"
FINAL_SCHEMA="${OUTPUT_DIR}/patients_schema.yaml"

# Activate the existing linkml environment
source /Users/alabarga/code/environments/linkml-env/bin/activate

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "=========================================================="
echo " Generating LinkML Schema for Patients Data               "
echo "=========================================================="
echo ""

echo "➡️ Extracting schema from patients.csv..."

# Convert CSV to TSV to guarantee correct LinkML parsing
TMP_TSV="/tmp/patients_$$.tsv"
python3 -c "import csv, sys; csv.writer(sys.stdout, delimiter='\t').writerows(csv.reader(sys.stdin))" < "$DATA_DIR/patients.csv" > "$TMP_TSV"

# Run Schema Automator to infer the LinkML schema just for patients.csv
schemauto generalize-tsv --class-name Patients "$TMP_TSV" > "$RAW_SCHEMA"

rm -f "$TMP_TSV"

echo "  ✓ Generated raw schema: $RAW_SCHEMA"
echo ""

echo "➡️ Enriching slots with OMOP-CDM required structure..."

# Run the python script to append description, imported_from, range, identifier, and required fields
python3 enrich_schema.py "$RAW_SCHEMA" "$FINAL_SCHEMA"

echo "  ✓ Generated final enriched schema: $FINAL_SCHEMA"
echo ""

echo "=========================================================="
echo " Process completed successfully!                        "
echo "=========================================================="
