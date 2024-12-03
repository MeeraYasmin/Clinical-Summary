from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

# Read the unstructured text file
file_path = "medical_data.txt"
with open(file_path, "r") as file:
    unstructured_text = file.read()

# Split the text into manageable chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
texts = text_splitter.split_text(unstructured_text)

# Convert the chunks into Document objects (LangChain's input format)
documents = [Document(page_content=text) for text in texts]

# Define a simple summarizer function
def local_summarizer(documents):
    """
    A basic local summarizer function that combines document chunks into a summary.
    """
    summary = []
    for doc in documents:
        content = doc.page_content
        # Here, a simple heuristic is used: take the first and last sentences of each chunk.
        sentences = content.split(". ")
        summary.append(sentences[0])  # First sentence
        if len(sentences) > 1:
            summary.append(sentences[-1])  # Last sentence
    return " ".join(summary)

# Generate the summary
summary = local_summarizer(documents)

# Display the summary
print("Extracted Summary:")
print(summary)
