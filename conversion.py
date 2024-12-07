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

# Define a prompt to convert the summary into FHIR resources
prompt = f"""
The following text contains a summary of clinical data:
{summary_data}

Please convert this clinical summary into the following FHIR resources, even if some data is missing:
- Patient
- Observation
- Practitioner
- AllergyIntolerance
- Problem
- Procedure
- FamilyMemberHistory
- MedicationStatement
- CarePlan

If the information for any field is missing, please provide "Not specified" for that field. If no information is provided for a resource, leave it empty or include "Not specified".

Here are the specific fields to include in each resource:

1. **Patient**: Include Name, Age, Gender, Date of Birth, and any other demographic information. If any data is missing, return "Not specified".
2. **Observation**: Include relevant clinical findings such as lab results (e.g., hemoglobin levels), if present. For missing findings, return "Not specified".
3. **Practitioner**: Include the name of the practitioner. If the practitioner name is not available, return "Not specified".
4. **AllergyIntolerance**: Include any known allergies or intolerances. If allergies are not mentioned, return "Not specified".
5. **Problem**: Include the diagnosis or any active conditions (e.g., Peptic ulcer disease). If not mentioned, return "Not specified".
6. **Procedure**: Include any performed procedures (e.g., upper endoscopy). If no procedures are listed, return "Not specified".
7. **FamilyMemberHistory**: Include any family medical history if mentioned. If not mentioned, return "Not specified".
8. **MedicationStatement**: Include all medications prescribed (e.g., pantoprazole, clarithromycin). If no medications are mentioned, return "Not specified".
9. **CarePlan**: Include the treatment plan, follow-up visits, and lifestyle recommendations. If no treatment or follow-up is mentioned, return "Not specified".

Please return the resources in structured JSON format as per the official FHIR specifications.
"""

# Query the model
response = llm.invoke([HumanMessage(content=prompt)])

# Print the response (FHIR resources in JSON format)
print("FHIR Resources in JSON Format:")
print(response.content)

# Optionally save the output to a file
with open("FHIR_Resources.json", "w") as file:
    file.write(response.content)