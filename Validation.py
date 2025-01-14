from langchain_openai.embeddings import OpenAIEmbeddings
from scipy.spatial.distance import cosine
import os

# Set your OpenAI API Key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

# Function to read the contents of a file
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Load data from the files
unstructured_data = read_file("medical_data.txt")  # Original unstructured text
structured_summary = read_file("Summary_data.txt")  # Structured output

# Initialize OpenAI Embeddings via LangChain
embeddings = OpenAIEmbeddings()

# Generate embeddings for the unstructured and structured text
unstructured_embedding = embeddings.embed_query(unstructured_data)
structured_embedding = embeddings.embed_query(structured_summary)

# Calculate cosine similarity as the confidence score
confidence_score = 1 - cosine(unstructured_embedding, structured_embedding)

# Output the confidence score
print(f"Confidence Score between 'medical_data.txt' and 'Summary_data.txt': {confidence_score:.4f}")
