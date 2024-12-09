from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Set your OpenAI API key
api_key = "your_api_key"

# Initialize the ChatOpenAI model with the API key
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=api_key  # Pass the API key here
)

# Read the content of the Summary_data.txt file
with open("Summary_data.txt", "r") as file:
    summary_data = file.read()

# Define a prompt to convert the summary into FHIR resources with full structures
prompt = f"""
The following text contains a summary of clinical data:
{summary_data}

Please convert this clinical summary into the following FHIR resources with full substructures as per the FHIR specification:
- Patient
- Observation
- Practitioner
- AllergyIntolerance
- Problem
- Procedure
- FamilyMemberHistory
- MedicationStatement
- CarePlan

### Resource Requirements
Ensure that all fields, subfields, and substructures are included in the output JSON for each resource. Use the FHIR JSON template for each resource type provided in the official FHIR documentation (https://www.hl7.org/fhir/). If a specific field or substructure is missing, include "Not specified" or an empty array where applicable.
1.Patient: Extract the following Fields: id, name, age, gender, birthDate, address, contact details, and other demographic details.
If any field is missing, include "Not specified".

2.Observation: Include Fields: id, status, code, subject, effectiveDateTime or effectivePeriod, value[x], interpretation, and related.
For missing fields, include "Not specified".

3.Practitioner: Extract Fields: id, name, identifier, qualification, and contact.
For missing data, include "Not specified".

4.AllergyIntolerance: Extract any known allergies or intolerances using:Fields: id, clinicalStatus, verificationStatus, code, patient, onset[x], note, and reaction.
For missing data, include "Not specified".

5.Problem: Extract as a Condition resource:Fields: id, clinicalStatus, verificationStatus, code, severity, patient, onset[x], note, and evidence.
If any data is missing, include "Not specified".

6.Procedure: Extract details for performed procedures using:Fields: id, status, code, subject, performed[x], performer, location, and note.
For missing data, include "Not specified".

7.FamilyMemberHistory: Extract:Fields: id, patient, relationship, conditions, and note.
For missing fields, include "Not specified".

8.MedicationStatement:Include all prescribed, ongoing, or historical medications.
Key Fields:id, status, medication (name and strength), subject, effective[x], dateAsserted, informationSource, and reason.
Detailed Dosage Information:renderedDosageInstruction: Full dosage instructions (e.g., "Take 1 tablet once daily in the morning").doseQuantity: Include value, unit, system, and code (e.g., "40 mg").frequency: Frequency of medication (e.g., "once daily").route: Administration route (e.g., "oral").timing: Time of administration (e.g., "morning").doseAndRate: Any rate-related dosing instructions.
Ensure all medications are parsed, even if partial details are available.For missing fields, include "Not specified".

9.CarePlan:Include:Core Fields: id, status, intent, category, subject, description, period, and activity.
Activity Details:steps: Specific treatment actions (e.g., lifestyle modifications, follow-up visits).
medications: List all medications (e.g., Pantoprazole, Clarithromycin, Amoxicillin, Ferrous sulfate).
Cross-reference these medications with MedicationStatement to confirm dosage, timing, and route details.
followUps: Scheduled visits or next steps.
If any field is missing, include "Not specified".
In activity, add specific steps, including medications to be taken, lifestyle recommendations, and follow-ups.
If medications are associated with the care plan, ensure they align with MedicationStatement details. If no treatment or follow-up is mentioned, return "Not specified".

If the information for any field is missing, please provide "Not specified" for that field. If no information is provided for a resource, leave it empty or include "Not specified".

### Output Format
Return all resources in structured JSON format conforming to the FHIR standard. Ensure the inclusion of detailed fields and substructures.
"""

# Query the model
response = llm.invoke([HumanMessage(content=prompt)])

# Print the response (FHIR resources in JSON format)
print("FHIR Resources in JSON Format:")
print(response.content)

# Optionally save the output to a file
with open("FHIR_Resources0.json", "w") as file:
    file.write(response.content)
