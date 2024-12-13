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

# Read the content of the uploaded medical data file
with open("medical_data.txt", "r") as file:
    medical_data = file.read()

# Define a prompt to extract clinical data summary
prompt = f"""
You are an expert medical professional tasked with analyzing unstructured clinical data. 
The text provided contains medical details about a patient. Please summarize the information thoroughly, 
ensuring no important or significant details are missed. Your summary should include, but not be limited to, 
the following sections:

From the given unstructured medical data:
{medical_data}

Please provide a comprehensive summary of all relevant clinical information, ensuring no significant detail is missed. Include the following details:

1. Patient Demographics: Name, age, gender, date of birth, and any other personal details mentioned.
2. Chief Complaint: The primary reason(s) for the patient's visit or hospitalization.
3. History of Present Illness: Details about the duration, progression, and symptoms of the current condition.
4. Past Medical History: All relevant prior diagnoses, treatments, surgeries, or conditions.
5. Family Medical History: Any significant health issues in family members.
6. Social History: Smoking, alcohol use, occupation, or lifestyle factors impacting health.
7. Clinical Findings: Key observations, lab results, diagnostic test findings, imaging results, and vital signs.
8. Diagnosis: Any diagnosed conditions or suspected conditions.
9. Treatment Plan: Medications, dosages, procedures, lifestyle recommendations, and follow-up plans.
10. Procedures Performed: Details of surgeries, diagnostic tests, or therapeutic procedures performed.
11. Allergies: Known allergies or intolerances to medications, foods, or other substances.
12. Progress Notes: Patient's response to treatments, changes in condition, and current status.
13. Medications: A detailed list of all medications prescribed, including dosages and administration instructions.
14. Prognosis: Expected outcomes, recovery timelines, and any risks or complications.
15. Additional Notes: Any other significant data that does not fit into the categories above.
16. Practitioner Details: Include the names, roles, and actions of the practitioners involved in the patient's care, such as prescribing medications, performing procedures, or managing treatment.

Please format the output into a clear and organized summary, ensuring that all significant information is extracted from the text provided.

"""

# Query the model
response = llm.invoke([HumanMessage(content=prompt)])

# Print the response
print("Comprehensive Medical Summary:")
print(response.content)

# Optionally save the output to a file
with open("Summary_data.txt", "w") as file:
    file.write(response.content)

