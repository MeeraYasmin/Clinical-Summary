from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Set your OpenAI API key
api_key = "your_open_api_key"

# Initialize the ChatOpenAI model with the API key
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=api_key
)

# Read the content of the unstructured medical data
with open("medical_data.txt", "r") as file:
    medical_data = file.read()

# Improved Prompt
prompt = f"""
You are an expert medical professional tasked with analyzing unstructured clinical data. 
The text below contains details about a patient's hospital stay. Extract and summarize all clinically relevant information in a structured manner.

Make sure to:
- Include **patient demographics** (infer approximate DOB from age/date if needed).
- State the **chief complaint** and symptoms clearly.
- Provide a detailed **history of present illness (HPI)**, including timeline and progression of symptoms.
- Extract **all lab/imaging/test results**, even if they are normal or within the reference range.
- List **all current and past diagnoses**, and if applicable, the suspected or confirmed etiology of the condition.
- Specify **procedures performed** with dates, and details on any relevant findings.
- List **medications** with dosage, frequency, and duration, including any planned tapering schedules.
- Mention **follow-up plans** and next appointment date if available.
- Identify **practitioners involved** (name(s), role(s), and contact information if available), or state “Not specified”.
- Highlight **social history**, **family history**, and any **known allergies**.
- Include relevant **prognosis**, **lifestyle/dietary recommendations**, and specific instructions for ongoing care (e.g., stress management, exercise recommendations).
  
Ensure that the following **dates** are included where relevant:
- **Admission Date**
- **Discharge Date**
- **Procedure Dates** (e.g., Endoscopy, Imaging, Surgery Dates)
- **Follow-up Date** (if available).

If any data is missing, specify "Not mentioned in the text." 

Include **hospitalization outcome** (discharge status) and a clear note on **medication duration** (e.g., duration of antibiotics, PPIs, etc.). If tapering is recommended, include detailed tapering instructions if mentioned. 

For any medical condition, whether infectious, chronic, acute, or procedural, ensure that:
- **Clinical Findings** (e.g., symptoms, physical exam findings, test results) are noted.
- **Diagnosis** includes both suspected and confirmed diagnoses based on available information.
- **Treatment Plan** is detailed, including medications, therapies, and lifestyle changes.
- If applicable, consider **patient education** and the importance of adherence to the prescribed regimen.

Format the output under the following sections:
1. Patient Demographics  
2. Chief Complaint  
3. History of Present Illness  
4. Past Medical History  
5. Family Medical History  
6. Social History  
7. Clinical Findings  
8. Diagnosis  
9. Treatment Plan  
10. Procedures Performed  
11. Allergies  
12. Progress Notes  
13. Medications  
14. Prognosis  
15. Additional Notes  
16. Practitioner Details  

Unstructured Medical Data:
{medical_data}
"""


# Query the model
response = llm.invoke([HumanMessage(content=prompt)])

# Output the response
print("Improved Medical Summary:\n")
print(response.content)

# Save the improved summary
with open("Improved_Summary_data.txt", "w") as file:
    file.write(response.content)
