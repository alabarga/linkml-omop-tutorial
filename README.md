# Declarative Data Standardization to OMOP-CDM using LinkML

**Alberto Labarga**  
*Barcelona Supercomputing Center*

## Abstract
This tutorial introduces a novel, declarative, and AI-augmented approach to standardizing clinical data to the OMOP Common Data Model using the LinkML ecosystem. Participants will learn to formally model source data, leverage AI to generate transformation logic, and execute and validate data mappings, transforming a resource-intensive ETL process into a reproducible and scalable knowledge-driven task.

## Keywords
OMOP-CDM, LinkML, Data Standardization, ETL, AI-augmented

## Introduction 
The secondary use of clinical data for research is severely constrained by data heterogeneity. While the OMOP Common Data Model (OMOP-CDM) provides a robust standard, the Extract-Transform-Load (ETL) process remains a manual, resource-intensive, and brittle bottleneck.

This tutorial introduces a paradigm shift, reframing data standardization from an imperative scripting task (e.g., writing custom SQL or Python) to a declarative, model-driven, and AI-augmented process. We will leverage the Linked Data Modeling Language (LinkML) ecosystem to achieve this.

In this hands-on session, participants will use LinkML to first create a formal, machine-readable schema for a synthetic source dataset (e.g., laboratory results). We will then review a canonical LinkML model of the target OMOP-CDM schema. With both source and target structures formally defined, we will demonstrate how this "structure-to-structure" mapping problem becomes highly amenable to automation. Participants will use a simple Python script—simulating the "cognitive core" of an agentic architecture—to automatically generate a declarative `linkml-map` specification. This map externalizes the transformation logic into a human-readable, verifiable, and executable format. Finally, participants will use the `linkml-map` library to execute this map, transforming the source data, and then use `linkml-validate` to rigorously check the output for compliance with the OMOP-CDM standard.

## Audience
This tutorial is addressed to data engineers, bioinformaticians, data stewards, clinical researchers, and data scientists who are involved in standardizing health data for research, particularly to the OMOP-CDM. It is ideal for anyone seeking more reproducible, scalable, and maintainable alternatives to traditional ETL pipelines.

## Learning Outcomes
At the end of this tutorial, participants are expected to:

- Understand the limitations of traditional, imperative ETL pipelines for OMOP-CDM standardization.
- Grasp the concepts of a declarative, model-driven approach to data mapping.
- Be able to write a basic LinkML schema to model a source dataset.
- Understand the structure and utility of a `linkml-map` declarative mapping specification.
- Gain experience in using a simple AI-augmented script (simulating an "agent") to generate this transformation map by comparing source and target schemas.
- Successfully execute a data transformation using the `linkml-map` library.
- Rigorously validate the transformed data against the target OMOP-CDM LinkML schema using `linkml-validate`.

## Prerequisites

### Knowledge / Competencies
- Participants are expected to have basic familiarity with Python programming (e.g., running scripts, managing simple environments).
- Basic understanding of data modeling concepts (e.g., what is a schema, a class, an attribute/slot).
- Familiarity with common data formats like CSV/JSON and markup languages like YAML.
- No prior expertise in LinkML or OMOP-CDM is required, though a general understanding of the OMOP-CDM's purpose will be beneficial.

### Technical
- Participants are required to have their own computer with an Internet connection.
- A modern web browser and the ability to run Python scripts (e.g., via VS Code, Jupyter, or a terminal) are necessary. All required Python libraries will be installable via `pip`.

## Tutorial Schedule (3.5 hours)

- **Part 1: Introduction (30 min)**
  - Welcome and tutor introductions.
  - The Standardization Bottleneck: Why is mapping to OMOP-CDM so hard?
  - A Paradigm Shift: From imperative scripts to declarative, AI-generated knowledge.
  - Introduction to the LinkML Ecosystem: `linkml`, `linkml-map`, and `linkml-validate`.

- **Part 2: Modeling the Schemas (60 min)**
  - **Hands-on:** Participants will model a synthetic source dataset (e.g., `labevents.csv`) by writing a `source_lab_schema.yaml` file from scratch.
  - **Review:** We will explore the pre-built, canonical LinkML schema for the target OMOP-CDM (`omop_cdm.yaml`).
  - **Discussion:** Defining the "structure-to-structure" reasoning problem for AI.

*Coffee Break (30 min)*

- **Part 3: Generating the Transformation Map (60 min)**
  - Introduction to the `linkml-map` specification: How to define class and slot derivations.
  - **Hands-on:** Participants will run a Python script (simulating the "Model Alignment Agent") that analyzes the source and target LinkML schemas and automatically generates a `lab_to_measurement.map.yaml` file.
  - **Review:** We will inspect the AI-generated map, emphasizing the human's role as an expert validator.

- **Part 4: Execution, Validation, and Wrap-up (30 min)**
  - **Hands-on:** Participants will use the `linkml-map` Python library to execute the generated map file on the source `patients.csv` data.
  - **Hands-on:** We will use `linkml-validate` to check the integrity of the output data against the target `omop_cdm.yaml` schema.
  - Final discussion, Q&A, and links to further resources.

## References

1. Hripcsak, G., Duke, J. D., Shah, N. H., et al. (2015). Observational Health Data Sciences and Informatics (OHDSI): Opportunities for Observational Researchers. *Studies in Health Technology and Informatics*, 216, 574–578.
2. Moxon, S. T., Solbrig, H. R., Unni, D. R., Jiao, D., Bruskiewich, R. M., Balhoff, J. P., Vaidya, G., Duncan, W. D., Hegde, H. B., Miller, M., Brush, M. H., Harris, N. L., Haendel, M. A., & Mungall, C. J. (2021). The Linked Data Modeling Language (LinkML): A General-Purpose Data Modeling Framework Grounded in Machine-Readable Semantics. In *International Conference on Biomedical Ontology*.
3. Adams, M. C. B., Perkins, M. L., Hudson, C., Madhira, V., Akbilgic, O., Ma, D., Hurley, R. W., & Topaloglu, U. (2025). Breaking Digital Health Barriers Through a Large Language Model–Based Tool for Automated Observational Medical Outcomes Partnership Mapping: Development and Validation Study. *Journal of Medical Internet Research*, 27, e69004. 
4. Labarga, A. (2025). An Agentic Architecture for Scalable and Reproducible Data Standardization to OMOP CDM using Declarative Modeling. *Artificial Intelligence in Biomedicine, CIABiomed 2025*

## Documentation in this repository

- [Profiling Synthea CSVs to LinkML](docs/PROFILE.md)
- [Hand-authored linkml-map basics (Patients → OMOP)](docs/MAP.md)
- [**LLM-assisted map generation** (using BAML)](docs/BAML.md)

## Online Resources

- [OMOP-CDM documentation](https://ohdsi.github.io/CommonDataModel/)
- [BAML Documentation](https://docs.boundaryml.com/home)
- [LinkML Documentation](https://linkml.io/linkml/)
- [LinkML-Map Documentation](https://linkml.io/linkml-map/)
