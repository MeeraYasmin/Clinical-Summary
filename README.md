# Clinical Data Extractor using LLMs and FHIR

This project extracts structured clinical data from unstructured discharge summaries or progress notes using Large Language Models (LLMs) and stores it in a FHIR-compliant format in a database.
---
## Overview

Healthcare data often exists in unstructured formats like discharge summaries or clinical notes. This project uses LLMs and prompt engineering (via LangChain) to:
1. Generate synthetic discharge summaries.
2. Extract relevant clinical entities using LLMs.
3. Convert the extracted data into FHIR (Fast Healthcare Interoperability Resources) format.
4. Store the FHIR data in PostgreSQL database.
The final goal is to create an open-source prototype to support healthcare interoperability using modern AI techniques.
---
## Tech Stack
- **LLMs**: OpenAI GPT
- **LangChain**: For prompt engineering and orchestration
- **FHIR Standard**: [HL7 FHIR](https://www.hl7.org/fhir/)
- **Python**: Backend processing
- **Database**: PostgreSQL
- **fhir.resources**: Python library to work with FHIR data models
- **GitHub**: Version control and project hosting
---
##  Workflow Steps
1. **Generate synthetic discharge summaries or progress notes** using ChatGPT
2. **Use LangChain and prompt engineering** to extract clinical entities from the notes.
3. **Map extracted data into FHIR resources**, including:
    - Patient
    - Observation
    - Practitioner
    - AllergyIntolerance
    - Problem
    - Procedure
    - FamilyMemberHistory
    - MedicationStatement
    - CarePlan
4. **Store FHIR-formatted data** in PostgreSQL.
5. **Version and host the project** on GitHub for public collaboration.
---
