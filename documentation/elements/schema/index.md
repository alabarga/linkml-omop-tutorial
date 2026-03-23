# omop_cdm_v54

A schema representing the OMOP CDM v5.4

URI: omop_cdm_v54

Name: omop_cdm_v54



## Classes

| Class | Description |
| --- | --- |
| [CareSite](CareSite.md) | The CARE_SITE table contains a list of uniquely identified institutional (phy... |
| [CdmSource](CdmSource.md) | The CDM_SOURCE table contains detail about the source database and the proces... |
| [Cohort](Cohort.md) | The subject of a cohort can have multiple, discrete records in the cohort tab... |
| [CohortDefinition](CohortDefinition.md) | The COHORT_DEFINITION table contains records defining a Cohort derived from t... |
| [ConditionEra](ConditionEra.md) | A Condition Era is defined as a span of time when the Person is assumed to ha... |
| [ConditionOccurrence](ConditionOccurrence.md) | Conditions are records of a Person suggesting the presence of a disease or me... |
| [Cost](Cost.md) | The COST table captures records containing the cost of any medical event reco... |
| [Death](Death.md) | The death domain contains the clinical event for how and when a Person dies |
| [DeviceExposure](DeviceExposure.md) | The ''Device'' domain captures information about a person''s exposure to a fo... |
| [DoseEra](DoseEra.md) | A Dose Era is defined as a span of time when the Person is assumed to be expo... |
| [DrugEra](DrugEra.md) | A Drug Era is defined as a span of time when the Person is assumed to be expo... |
| [DrugExposure](DrugExposure.md) | The Drug domain captures records about the utilization of a Drug when ingeste... |
| [Episode](Episode.md) | The EPISODE table aggregates lower-level clinical events (VISIT_OCCURRENCE, D... |
| [EpisodeEvent](EpisodeEvent.md) | The EPISODE_EVENT table connects qualifying clinical events (such as CONDITIO... |
| [FactRelationship](FactRelationship.md) | The FACT_RELATIONSHIP table contains records about the relationships between ... |
| [Location](Location.md) | The LOCATION table represents a generic way to capture physical location or a... |
| [Measurement](Measurement.md) | The MEASUREMENT table contains records of Measurement, i |
| [Metadata](Metadata.md) | The METADATA table contains metadata information about a dataset that has bee... |
| [Note](Note.md) | The NOTE table captures unstructured information that was recorded by a provi... |
| [NoteNlp](NoteNlp.md) | The NOTE_NLP table will encode all output of NLP on clinical notes |
| [Observation](Observation.md) | The OBSERVATION table captures clinical facts about a Person obtained in the ... |
| [ObservationPeriod](ObservationPeriod.md) | The OBSERVATION_PERIOD table contains records which uniquely define the spans... |
| [PayerPlanPeriod](PayerPlanPeriod.md) | The PAYER_PLAN_PERIOD table captures details of the period of time that a Per... |
| [Person](Person.md) | The Person Domain contains records that uniquely identify each patient in the... |
| [ProcedureOccurrence](ProcedureOccurrence.md) | The PROCEDURE_OCCURRENCE table contains records of activities or processes or... |
| [Provider](Provider.md) | The PROVIDER table contains a list of uniquely identified healthcare provider... |
| [Specimen](Specimen.md) | The specimen domain contains the records identifying biological samples from ... |
| [VisitDetail](VisitDetail.md) | The VISIT_DETAIL table is an optional table used to represents details of eac... |
| [VisitOccurrence](VisitOccurrence.md) | The VISIT_OCCURRENCE table contains the spans of time a Person continuously r... |



## Slots

| Slot | Description |
| --- | --- |
| [address_1](address_1.md) | The address field 1, typically used for the street address, as it appears in ... |
| [address_2](address_2.md) | The address field 2, typically used for additional detail such as buildings, ... |
| [admitted_from_concept_id](admitted_from_concept_id.md) | A foreign key to the predefined concept in the Place of Service Vocabulary re... |
| [admitted_from_source_value](admitted_from_source_value.md) | The source code for where the patient was admitted from as it appears in the ... |
| [amount_allowed](amount_allowed.md) | The contracted amount agreed between the payer and provider |
| [anatomic_site_concept_id](anatomic_site_concept_id.md) | A foreign key to a Standard Concept identifier for the anatomic location of s... |
| [anatomic_site_source_value](anatomic_site_source_value.md) | The information about the anatomic site as detailed in the source |
| [birth_datetime](birth_datetime.md) | The date and time of birth of the person |
| [care_site_id](care_site_id.md) | A foreign key to the site of primary care in the care_site table, where the d... |
| [care_site_name](care_site_name.md) | The verbatim description or name of the Care Site as in data source |
| [care_site_source_value](care_site_source_value.md) | The identifier for the Care Site in the source data, stored here for referenc... |
| [cause_concept_id](cause_concept_id.md) | This is the Standard Concept representing the Person's  cause of death, if av... |
| [cause_source_concept_id](cause_source_concept_id.md) | If the cause of death was coded using a Vocabulary present in the OMOP Vocabu... |
| [cause_source_value](cause_source_value.md) | If available, put the source code representing the cause of death here |
| [cdm_etl_reference](cdm_etl_reference.md) | URL or other external reference to location of ETL specification documentatio... |
| [cdm_holder](cdm_holder.md) | The name of the organization responsible for the development of the CDM insta... |
| [cdm_release_date](cdm_release_date.md) | The date when the CDM was instantiated |
| [cdm_source_abbreviation](cdm_source_abbreviation.md) | An abbreviation of the name |
| [cdm_source_name](cdm_source_name.md) | The full name of the source |
| [cdm_version](cdm_version.md) | The version of CDM used |
| [cdm_version_concept_id](cdm_version_concept_id.md) | The Concept Id representing the version of the CDM |
| [city](city.md) | The city field as it appears in the source data |
| [cohort_definition_description](cohort_definition_description.md) | A complete description of the cohort |
| [cohort_definition_id](cohort_definition_id.md) | A foreign key to a record in the COHORT_DEFINITION table containing relevant ... |
| [cohort_definition_name](cohort_definition_name.md) | A short description of the cohort |
| [cohort_definition_syntax](cohort_definition_syntax.md) | Syntax or code to operationalize the Cohort Definition |
| [cohort_end_date](cohort_end_date.md) | The date when the Cohort Definition criteria for the Person, Provider or Visi... |
| [cohort_initiation_date](cohort_initiation_date.md) | A date to indicate when the Cohort was initiated in the COHORT table |
| [cohort_start_date](cohort_start_date.md) | The date when the Cohort Definition criteria for the Person, Provider or Visi... |
| [condition_concept_id](condition_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [condition_end_date](condition_end_date.md) | The date when the instance of the Condition is considered to have ended |
| [condition_end_datetime](condition_end_datetime.md) | The date and timewhen the instance of the Condition is considered to have end... |
| [condition_era_end_date](condition_era_end_date.md) | The end date for the Condition Era constructed from the individual instances ... |
| [condition_era_id](condition_era_id.md) | A unique identifier for each Condition Era |
| [condition_era_start_date](condition_era_start_date.md) | The start date for the Condition Era constructed from the individual instance... |
| [condition_occurrence_count](condition_occurrence_count.md) | The number of individual Condition Occurrences used to construct the conditio... |
| [condition_occurrence_id](condition_occurrence_id.md) | A unique identifier for each Condition Occurrence event |
| [condition_source_concept_id](condition_source_concept_id.md) | A foreign key to a Condition Concept that refers to the code used in the sour... |
| [condition_source_value](condition_source_value.md) | The source code for the Condition as it appears in the source data |
| [condition_start_date](condition_start_date.md) | The date when the instance of the Condition is recorded |
| [condition_start_datetime](condition_start_datetime.md) | The date and time when the instance of the Condition is recorded |
| [condition_status_concept_id](condition_status_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [condition_status_source_value](condition_status_source_value.md) | The source code for the condition status as it appears in the source data |
| [condition_type_concept_id](condition_type_concept_id.md) | A foreign key to the predefined Concept identifier in the Standardized Vocabu... |
| [cost_domain_id](cost_domain_id.md) | The concept representing the domain of the cost event, from which the corresp... |
| [cost_event_id](cost_event_id.md) | A foreign key identifier to the event (e |
| [cost_id](cost_id.md) | A unique identifier for each COST record |
| [cost_type_concept_id](cost_type_concept_id.md) | A foreign key identifier to a concept in the CONCEPT table for the provenance... |
| [country_concept_id](country_concept_id.md) | The Concept Id representing the country |
| [country_source_value](country_source_value.md) | The name of the country |
| [county](county.md) | The county |
| [currency_concept_id](currency_concept_id.md) | A foreign key identifier to the concept representing the 3-letter code used t... |
| [day_of_birth](day_of_birth.md) | The day of the month of birth of the person |
| [days_supply](days_supply.md) | The number of days of supply of the medication as prescribed |
| [dea](dea.md) | The Drug Enforcement Administration (DEA) number of the provider |
| [death_date](death_date.md) | The date of death of the person |
| [death_datetime](death_datetime.md) | The date and time of death of the person |
| [death_type_concept_id](death_type_concept_id.md) | This is the provenance of the death record, i |
| [definition_type_concept_id](definition_type_concept_id.md) | Type defining what kind of Cohort Definition the record represents and how th... |
| [device_concept_id](device_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [device_exposure_end_date](device_exposure_end_date.md) | The date use of the Device or supply was ceased |
| [device_exposure_end_datetime](device_exposure_end_datetime.md) | The date and time use of the Device or supply was ceased |
| [device_exposure_id](device_exposure_id.md) | A system-generated unique identifier for each Device Exposure |
| [device_exposure_start_date](device_exposure_start_date.md) | The date the Device or supply was applied or used |
| [device_exposure_start_datetime](device_exposure_start_datetime.md) | The date and time the Device or supply was applied or used |
| [device_source_concept_id](device_source_concept_id.md) | A foreign key to a Device Concept that refers to the code used in the source |
| [device_source_value](device_source_value.md) | The source code for the Device as it appears in the source data |
| [device_type_concept_id](device_type_concept_id.md) | A foreign key to the predefined Concept identifier in the Standardized Vocabu... |
| [discharged_to_concept_id](discharged_to_concept_id.md) | A foreign key to the predefined concept in the Place of Service Vocabulary re... |
| [discharged_to_source_value](discharged_to_source_value.md) | The source code for the discharge disposition as it appears in the source dat... |
| [disease_status_concept_id](disease_status_concept_id.md) | A foreign key to a Standard Concept identifier for the Disease Status of spec... |
| [disease_status_source_value](disease_status_source_value.md) | The information about the disease status as detailed in the source |
| [domain_concept_id_1](domain_concept_id_1.md) | The concept representing the domain of fact one, from which the corresponding... |
| [domain_concept_id_2](domain_concept_id_2.md) | The concept representing the domain of fact two, from which the corresponding... |
| [dose_era_end_date](dose_era_end_date.md) | The date the Person was no longer exposed to the dosage of the specific drug ... |
| [dose_era_id](dose_era_id.md) | A unique identifier for each Dose Era |
| [dose_era_start_date](dose_era_start_date.md) | The date the Person started on the specific dosage, with at least 31 days sin... |
| [dose_unit_source_value](dose_unit_source_value.md) | The information about the dose unit as detailed in the source |
| [dose_value](dose_value.md) | The numeric value of the dose |
| [drg_concept_id](drg_concept_id.md) | A foreign key referring to a Standard Concept ID in the Standardized Vocabula... |
| [drg_source_value](drg_source_value.md) | The source value for the 3-digit DRG source code as it appears in the source ... |
| [drug_concept_id](drug_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [drug_era_end_date](drug_era_end_date.md) | The Drug Era End Date is the end date of the last Drug Exposure |
| [drug_era_id](drug_era_id.md) | A unique identifier for each Drug Era |
| [drug_era_start_date](drug_era_start_date.md) | The Drug Era Start Date is the start date of the first Drug Exposure for a gi... |
| [drug_exposure_count](drug_exposure_count.md) | The number of individual Drug Exposure occurrences used to construct the Drug... |
| [drug_exposure_end_date](drug_exposure_end_date.md) | The end date for the current instance of Drug utilization |
| [drug_exposure_end_datetime](drug_exposure_end_datetime.md) | The end date and time for the current instance of Drug utilization |
| [drug_exposure_id](drug_exposure_id.md) | A system-generated unique identifier for each Drug utilization event |
| [drug_exposure_start_date](drug_exposure_start_date.md) | The start date for the current instance of Drug utilization |
| [drug_exposure_start_datetime](drug_exposure_start_datetime.md) | The start date and time for the current instance of Drug utilization |
| [drug_source_concept_id](drug_source_concept_id.md) | A foreign key to a Drug Concept that refers to the code used in the source |
| [drug_source_value](drug_source_value.md) | The source code for the Drug as it appears in the source data |
| [drug_type_concept_id](drug_type_concept_id.md) | A foreign key to the predefined Concept identifier in the Standardized Vocabu... |
| [encoding_concept_id](encoding_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [episode_concept_id](episode_concept_id.md) | The EPISODE_CONCEPT_ID represents the kind abstraction related to the disease... |
| [episode_end_date](episode_end_date.md) | The date when the instance of the Episode is considered to have ended |
| [episode_end_datetime](episode_end_datetime.md) | The date when the instance of the Episode is considered to have ended |
| [episode_event_field_concept_id](episode_event_field_concept_id.md) | This field is the CONCEPT_ID that identifies which table the primary key of t... |
| [episode_id](episode_id.md) | A unique identifier for each Episode |
| [episode_number](episode_number.md) | For sequences of episodes, this is used to indicate the order the episodes oc... |
| [episode_object_concept_id](episode_object_concept_id.md) | A Standard Concept representing the disease phase, outcome, or other abstract... |
| [episode_parent_id](episode_parent_id.md) | Use this field to find the Episode that subsumes the given Episode record |
| [episode_source_concept_id](episode_source_concept_id.md) | A foreign key to a Episode Concept that refers to the code used in the source |
| [episode_source_value](episode_source_value.md) | The source code for the Episode as it appears in the source data |
| [episode_start_date](episode_start_date.md) | The date when the Episode beings |
| [episode_start_datetime](episode_start_datetime.md) | The date and time when the Episode begins |
| [episode_type_concept_id](episode_type_concept_id.md) | This field can be used to determine the provenance of the Episode record, as ... |
| [ethnicity_concept_id](ethnicity_concept_id.md) | A foreign key that refers to the standard concept identifier in the Standardi... |
| [ethnicity_source_concept_id](ethnicity_source_concept_id.md) | A foreign key to the ethnicity concept that refers to the code used in the so... |
| [ethnicity_source_value](ethnicity_source_value.md) | The source code for the ethnicity of the person as it appears in the source d... |
| [event_id](event_id.md) | This field is the primary key of the linked record in the database |
| [fact_id_1](fact_id_1.md) | The unique identifier in the table corresponding to the domain of fact one |
| [fact_id_2](fact_id_2.md) | The unique identifier in the table corresponding to the domain of fact two |
| [family_source_value](family_source_value.md) | The source code for the Person''s family as it appears in the source data |
| [gap_days](gap_days.md) | The number of days that are not covered by DRUG_EXPOSURE records that were us... |
| [gender_concept_id](gender_concept_id.md) | A foreign key that refers to an identifier in the CONCEPT table for the uniqu... |
| [gender_source_concept_id](gender_source_concept_id.md) | A foreign key to the gender concept that refers to the code used in the sourc... |
| [gender_source_value](gender_source_value.md) | The source code for the gender of the person as it appears in the source data |
| [language_concept_id](language_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [latitude](latitude.md) | The geocoded latitude |
| [lexical_variant](lexical_variant.md) | Raw text extracted from the NLP tool |
| [location_id](location_id.md) | A foreign key to the place of residency for the person in the location table,... |
| [location_source_value](location_source_value.md) | The verbatim information that is used to uniquely identify the location as it... |
| [longitude](longitude.md) | The geocoded longitude |
| [lot_number](lot_number.md) | An identifier assigned to a particular quantity or lot of Drug product from t... |
| [meas_event_field_concept_id](meas_event_field_concept_id.md) | If the Measurement record is related to another record in the database, this ... |
| [measurement_concept_id](measurement_concept_id.md) | A foreign key to the standard measurement concept identifier in the Standardi... |
| [measurement_date](measurement_date.md) | The date of the Measurement |
| [measurement_datetime](measurement_datetime.md) | The date and time of the Measurement |
| [measurement_event_id](measurement_event_id.md) | If the Measurement record is related to another record in the database, this ... |
| [measurement_id](measurement_id.md) | A unique identifier for each Measurement |
| [measurement_source_concept_id](measurement_source_concept_id.md) | A foreign key to a Concept in the Standard Vocabularies that refers to the co... |
| [measurement_source_value](measurement_source_value.md) | The Measurement name as it appears in the source data |
| [measurement_time](measurement_time.md) | The time of the Measurement |
| [measurement_type_concept_id](measurement_type_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [metadata_concept_id](metadata_concept_id.md) | OMOP Vocabulary CONCEPT_ID that identifies the information you with to track ... |
| [metadata_date](metadata_date.md) | The date associated with metadata |
| [metadata_datetime](metadata_datetime.md) | The date and time associated with metadata |
| [metadata_id](metadata_id.md) | The unique key given to a Metadata record |
| [metadata_type_concept_id](metadata_type_concept_id.md) | OMOP Vocabulary CONCEPT_ID that identifies the type information you with to t... |
| [modifier_concept_id](modifier_concept_id.md) | A foreign key to a Standard Concept identifier for a modifier to the Procedur... |
| [modifier_source_value](modifier_source_value.md) | The source code for the qualifier as it appears in the source data |
| [month_of_birth](month_of_birth.md) | The month of birth of the person |
| [name](name.md) | Name of the CONCEPT_ID stored in METADATA_CONCEPT_ID or in the event there is... |
| [nlp_date](nlp_date.md) | The date of the note processing |
| [nlp_datetime](nlp_datetime.md) | The date and time of the note processing |
| [nlp_system](nlp_system.md) | Name and version of the NLP system that extracted the term |
| [note_class_concept_id](note_class_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [note_date](note_date.md) | The date the note was recorded |
| [note_datetime](note_datetime.md) | The date and time the note was recorded |
| [note_event_field_concept_id](note_event_field_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [note_event_id](note_event_id.md) | A foreign key identifier to the event (e |
| [note_id](note_id.md) | A foreign key to the Note table note the term was |
| [note_nlp_concept_id](note_nlp_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [note_nlp_id](note_nlp_id.md) | A unique identifier for each term extracted from a note |
| [note_nlp_source_concept_id](note_nlp_source_concept_id.md) | A foreign key to a Concept that refers to the code in the source vocabulary u... |
| [note_source_value](note_source_value.md) | The source value associated with the origin of the Note |
| [note_text](note_text.md) | The content of the Note |
| [note_title](note_title.md) | The title of the Note as it appears in the source |
| [note_type_concept_id](note_type_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies refl... |
| [npi](npi.md) | The National Provider Identifier (NPI) of the provider |
| [obs_event_field_concept_id](obs_event_field_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [observation_concept_id](observation_concept_id.md) | A foreign key to the standard observation concept identifier in the Standardi... |
| [observation_date](observation_date.md) | The date of the observation |
| [observation_datetime](observation_datetime.md) | The date and time of the observation |
| [observation_event_id](observation_event_id.md) | A foreign key to an event table (e |
| [observation_id](observation_id.md) | A unique identifier for each observation |
| [observation_period_end_date](observation_period_end_date.md) | The end date of the observation period for which data are available from the ... |
| [observation_period_id](observation_period_id.md) | A unique identifier for each observation period |
| [observation_period_start_date](observation_period_start_date.md) | The start date of the observation period for which data are available from th... |
| [observation_source_concept_id](observation_source_concept_id.md) | A foreign key to a Concept that refers to the code used in the source |
| [observation_source_value](observation_source_value.md) | The observation code as it appears in the source data |
| [observation_type_concept_id](observation_type_concept_id.md) | A foreign key to the predefined concept identifier in the Standardized Vocabu... |
| [operator_concept_id](operator_concept_id.md) | A foreign key identifier to the predefined Concept in the Standardized Vocabu... |
| [paid_by_patient](paid_by_patient.md) | The total amount paid by the Person as a share of the expenses |
| [paid_by_payer](paid_by_payer.md) | The amount paid by the Payer for the goods or services |
| [paid_by_primary](paid_by_primary.md) | The amount paid by a primary Payer through the coordination of benefits |
| [paid_dispensing_fee](paid_dispensing_fee.md) | The amount paid by the Payer to a pharmacy for dispensing a drug, excluding t... |
| [paid_ingredient_cost](paid_ingredient_cost.md) | The amount paid by the Payer to a pharmacy for the drug, excluding the amount... |
| [paid_patient_coinsurance](paid_patient_coinsurance.md) | The amount paid by the Person as a joint assumption of risk |
| [paid_patient_copay](paid_patient_copay.md) | The amount paid by the Person as a fixed contribution to the expenses |
| [paid_patient_deductible](paid_patient_deductible.md) | The amount paid by the Person that is counted toward the deductible defined b... |
| [parent_visit_detail_id](parent_visit_detail_id.md) | Use this field to find the visit detail that subsumes the given visit detail ... |
| [payer_concept_id](payer_concept_id.md) | A foreign key that refers to a standard Payer concept identifier in the Stand... |
| [payer_plan_period_end_date](payer_plan_period_end_date.md) | The end date of the payer plan period |
| [payer_plan_period_id](payer_plan_period_id.md) | A foreign key to the PAYER_PLAN_PERIOD table, where the details of the Payer,... |
| [payer_plan_period_start_date](payer_plan_period_start_date.md) | The start date of the payer plan period |
| [payer_source_concept_id](payer_source_concept_id.md) | A foreign key to a payer concept that refers to the code used in the source |
| [payer_source_value](payer_source_value.md) | The source code for the payer as it appears in the source data |
| [period_type_concept_id](period_type_concept_id.md) | A foreign key identifier to the predefined concept in the Standardized Vocabu... |
| [person_id](person_id.md) | A unique identifier for each person |
| [person_source_value](person_source_value.md) | An (encrypted) key derived from the person identifier in the source data |
| [place_of_service_concept_id](place_of_service_concept_id.md) | A foreign key that refers to a Place of Service Concept ID in the Standardize... |
| [place_of_service_source_value](place_of_service_source_value.md) | The source code for the Place of Service as it appears in the source data, st... |
| [plan_concept_id](plan_concept_id.md) | A foreign key that refers to a standard plan concept identifier that represen... |
| [plan_source_concept_id](plan_source_concept_id.md) | A foreign key to a plan concept that refers to the plan code used in the sour... |
| [plan_source_value](plan_source_value.md) | The source code for the Person''s health benefit plan as it appears in the so... |
| [preceding_visit_detail_id](preceding_visit_detail_id.md) | A foreign key to the VISIT_DETAIL table of the visit immediately preceding th... |
| [preceding_visit_occurrence_id](preceding_visit_occurrence_id.md) | A foreign key to the VISIT_OCCURRENCE table of the visit immediately precedin... |
| [procedure_concept_id](procedure_concept_id.md) | A foreign key that refers to a standard procedure Concept identifier in the S... |
| [procedure_date](procedure_date.md) | The date on which the Procedure was performed |
| [procedure_datetime](procedure_datetime.md) | The date and time on which the Procedure was performed |
| [procedure_end_date](procedure_end_date.md) | The date the instance of the Procedure is considered to have ended |
| [procedure_end_datetime](procedure_end_datetime.md) | The date and timewhen the instance of the Procedure is considered to have end... |
| [procedure_occurrence_id](procedure_occurrence_id.md) | A system-generated unique identifier for each Procedure Occurrence |
| [procedure_source_concept_id](procedure_source_concept_id.md) | A foreign key to a Procedure Concept that refers to the code used in the sour... |
| [procedure_source_value](procedure_source_value.md) | The source code for the Procedure as it appears in the source data |
| [procedure_type_concept_id](procedure_type_concept_id.md) | A foreign key to the predefined Concept identifier in the Standardized Vocabu... |
| [production_id](production_id.md) | This is the Production Identifier (UDI-PI) portion of the Unique Device Ident... |
| [provider_id](provider_id.md) | A foreign key to the primary care provider the person is seeing in the provid... |
| [provider_name](provider_name.md) | A description of the Provider |
| [provider_source_value](provider_source_value.md) | The identifier used for the Provider in the source data, stored here for refe... |
| [qualifier_concept_id](qualifier_concept_id.md) | A foreign key to a Standard Concept ID for a qualifier (e |
| [qualifier_source_value](qualifier_source_value.md) | The source value associated with a qualifier to characterize the observation |
| [quantity](quantity.md) | The quantity of drug as recorded in the original prescription or dispensing r... |
| [race_concept_id](race_concept_id.md) | A foreign key that refers to an identifier in the CONCEPT table for the uniqu... |
| [race_source_concept_id](race_source_concept_id.md) | A foreign key to the race concept that refers to the code used in the source |
| [race_source_value](race_source_value.md) | The source code for the race of the person as it appears in the source data |
| [range_high](range_high.md) | The upper limit of the normal range of the Measurement |
| [range_low](range_low.md) | The lower limit of the normal range of the Measurement result |
| [refills](refills.md) | The number of refills after the initial prescription |
| [relationship_concept_id](relationship_concept_id.md) | A foreign key that refers to an identifier in the CONCEPT table for the uniqu... |
| [revenue_code_concept_id](revenue_code_concept_id.md) | A foreign key referring to a Standard Concept ID in the Standardized Vocabula... |
| [revenue_code_source_value](revenue_code_source_value.md) | The source value for the Revenue code as it appears in the source data, store... |
| [route_concept_id](route_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [route_source_value](route_source_value.md) | The information about the route of administration as detailed in the source |
| [section_concept_id](section_concept_id.md) | A foreign key to the predefined Concept in the Standardized Vocabularies repr... |
| [sig](sig.md) | The directions (''signetur'') on the Drug prescription as recorded in the ori... |
| [snippet](snippet.md) | A small window of text surrounding the term |
| [source_description](source_description.md) | A description of the source data origin and purpose for collection |
| [source_documentation_reference](source_documentation_reference.md) | URL or other external reference to location of source documentation |
| [source_release_date](source_release_date.md) | The date for which the source data are most current, such as the last day of ... |
| [specialty_concept_id](specialty_concept_id.md) | A foreign key to a Standard Specialty Concept ID in the Standardized Vocabula... |
| [specialty_source_concept_id](specialty_source_concept_id.md) | A foreign key to a Concept that refers to the code used in the source |
| [specialty_source_value](specialty_source_value.md) | The source code for the Provider specialty as it appears in the source data, ... |
| [specimen_concept_id](specimen_concept_id.md) | A foreign key referring to a Standard Concept identifier in the Standardized ... |
| [specimen_date](specimen_date.md) | The date the specimen was obtained from the Person |
| [specimen_datetime](specimen_datetime.md) | The date and time on the date when the Specimen was obtained from the person |
| [specimen_id](specimen_id.md) | A unique identifier for each specimen |
| [specimen_source_id](specimen_source_id.md) | The Specimen identifier as it appears in the source data |
| [specimen_source_value](specimen_source_value.md) | The Specimen value as it appears in the source data |
| [specimen_type_concept_id](specimen_type_concept_id.md) | A foreign key referring to the Concept identifier in the Standardized Vocabul... |
| [sponsor_concept_id](sponsor_concept_id.md) | A foreign key that refers to a concept identifier that represents the sponsor... |
| [sponsor_source_concept_id](sponsor_source_concept_id.md) | A foreign key to a sponsor concept that refers to the sponsor code used in th... |
| [sponsor_source_value](sponsor_source_value.md) | The source code for the Person''s sponsor of the health plan as it appears in... |
| [state](state.md) | The state field as it appears in the source data |
| [stop_reason](stop_reason.md) | The reason that the Condition was no longer present, as indicated in the sour... |
| [stop_reason_concept_id](stop_reason_concept_id.md) | A foreign key that refers to a standard termination reason that represents th... |
| [stop_reason_source_concept_id](stop_reason_source_concept_id.md) | A foreign key to a stop-coverage concept that refers to the code used in the ... |
| [stop_reason_source_value](stop_reason_source_value.md) | The reason for stop-coverage as it appears in the source data |
| [subject_concept_id](subject_concept_id.md) | This field contains a Concept that represents the domain of the subjects that... |
| [subject_id](subject_id.md) | A foreign key to the subject in the cohort |
| [term_exists](term_exists.md) | A summary modifier that signifies presence or absence of the term for a given... |
| [term_modifiers](term_modifiers.md) | For the modifiers that are there, they would have to have these values:  - Ne... |
| [term_temporal](term_temporal.md) | Term_temporal is to indicate if a condition is present or just in the past |
| [total_charge](total_charge.md) | The total amount charged by some provider of goods or services (e |
| [total_cost](total_cost.md) | The cost incurred by the provider of goods or services |
| [total_paid](total_paid.md) | The total amount actually paid from all payers for goods or services of the p... |
| [unique_device_id](unique_device_id.md) | A UDI or equivalent identifying the instance of the Device used in the Person |
| [unit_concept_id](unit_concept_id.md) | A foreign key that refers to a Standard Concept identifier in the Standardize... |
| [unit_source_concept_id](unit_source_concept_id.md) | This is the concept representing the UNIT_SOURCE_VALUE and may not necessaril... |
| [unit_source_value](unit_source_value.md) | The information about the Unit as detailed in the source |
| [value_as_concept_id](value_as_concept_id.md) | A foreign key to an observation result stored as a Concept ID |
| [value_as_number](value_as_number.md) | The observation result stored as a number |
| [value_as_string](value_as_string.md) | The observation result stored as a string |
| [value_source_value](value_source_value.md) | The source value associated with the content of the value_as_number or value_... |
| [verbatim_end_date](verbatim_end_date.md) | The known end date of a drug_exposure as provided by the source |
| [visit_concept_id](visit_concept_id.md) | A foreign key that refers to a visit Concept identifier in the Standardized V... |
| [visit_detail_concept_id](visit_detail_concept_id.md) | A foreign key that refers to a visit Concept identifier in the Standardized V... |
| [visit_detail_end_date](visit_detail_end_date.md) | The end date of the visit |
| [visit_detail_end_datetime](visit_detail_end_datetime.md) | The date and time of the visit end |
| [visit_detail_id](visit_detail_id.md) | A unique identifier for each Person''s visit or encounter at a healthcare pro... |
| [visit_detail_source_concept_id](visit_detail_source_concept_id.md) | A foreign key to a Concept that refers to the code used in the source |
| [visit_detail_source_value](visit_detail_source_value.md) | The source code for the visit as it appears in the source data |
| [visit_detail_start_date](visit_detail_start_date.md) | The start date of the visit |
| [visit_detail_start_datetime](visit_detail_start_datetime.md) | The date and time of the visit started |
| [visit_detail_type_concept_id](visit_detail_type_concept_id.md) | A foreign key to the predefined Concept identifier in the Standardized Vocabu... |
| [visit_end_date](visit_end_date.md) | The end date of the visit |
| [visit_end_datetime](visit_end_datetime.md) | The date and time of the visit end |
| [visit_occurrence_id](visit_occurrence_id.md) | A foreign key to the visit in the VISIT_OCCURRENCE table during which the Con... |
| [visit_source_concept_id](visit_source_concept_id.md) | A foreign key to a Concept that refers to the code used in the source |
| [visit_source_value](visit_source_value.md) | The source code for the visit as it appears in the source data |
| [visit_start_date](visit_start_date.md) | The start date of the visit |
| [visit_start_datetime](visit_start_datetime.md) | The date and time of the visit started |
| [visit_type_concept_id](visit_type_concept_id.md) | A foreign key to the predefined Concept identifier in the Standardized Vocabu... |
| [vocabulary_version](vocabulary_version.md) | Version of the OMOP standardised vocabularies loaded |
| [year_of_birth](year_of_birth.md) | The year of birth of the person |
| [zip](zip.md) | The zip or postal code |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [EncodingValues](EncodingValues.md) |  |
| [OmopConditionStatusValues](OmopConditionStatusValues.md) |  |
| [OmopConditionValues](OmopConditionValues.md) |  |
| [OmopDeviceValues](OmopDeviceValues.md) |  |
| [OmopDrugValues](OmopDrugValues.md) |  |
| [OmopEpisodeValues](OmopEpisodeValues.md) |  |
| [OmopEthnicityValues](OmopEthnicityValues.md) |  |
| [OmopGenderValues](OmopGenderValues.md) |  |
| [OmopGeographyValues](OmopGeographyValues.md) |  |
| [OmopMeasValue](OmopMeasValue.md) |  |
| [OmopMeasValueOperatorValues](OmopMeasValueOperatorValues.md) |  |
| [OmopMeasurementValues](OmopMeasurementValues.md) |  |
| [OmopMetadataValues](OmopMetadataValues.md) |  |
| [OmopModifierValues](OmopModifierValues.md) |  |
| [OmopPayerValues](OmopPayerValues.md) |  |
| [OmopPlanStopReasonValues](OmopPlanStopReasonValues.md) |  |
| [OmopPlanValues](OmopPlanValues.md) |  |
| [OmopProcedureValues](OmopProcedureValues.md) |  |
| [OmopProviderValues](OmopProviderValues.md) |  |
| [OmopRaceValues](OmopRaceValues.md) |  |
| [OmopRouteValues](OmopRouteValues.md) |  |
| [OmopSpecimenValues](OmopSpecimenValues.md) |  |
| [OmopTypeConceptValues](OmopTypeConceptValues.md) |  |
| [OmopUnitValues](OmopUnitValues.md) |  |
| [OmopVisitValues](OmopVisitValues.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
