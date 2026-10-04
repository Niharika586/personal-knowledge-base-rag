import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import ollama
import os

st.title("Personal Knowledge Base - RAG")

DOCUMENT_FOLDER = "documents"


# Load embedding model
@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


# Read PDF files
documents = []

for filename in os.listdir(DOCUMENT_FOLDER):

    if filename.lower().endswith(".pdf"):

        pdf_path = os.path.join(DOCUMENT_FOLDER, filename)

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        documents.append(text)


# Check documents
if not documents:
    st.warning("No PDF found in the documents folder.")
    st.stop()


# Combine PDF text
full_text = "\n".join(documents)


# Split text into chunks
chunk_size = 500

chunks = [
    full_text[i:i + chunk_size]
    for i in range(0, len(full_text), chunk_size)
]


st.success("PDF loaded successfully!")


# Create embeddings
document_embeddings = model.encode(chunks)


# Question input
question = st.text_input(
    "Ask a question about your document:"
)


if question:

    # Convert question to embedding
    question_embedding = model.encode([question])

    # Find similar chunks
    similarities = cosine_similarity(
        question_embedding,
        document_embeddings
    )[0]

    # Get best matching chunks
    top_indices = similarities.argsort()[-3:][::-1]

    relevant_text = "\n\n".join(
        chunks[index] for index in top_indices
    )


    # Send retrieved information to Llama
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the information
provided in the document context below.

If the answer is not present in the context,
say that the information is not available in the document.

Document context:
{relevant_text}

User question:
{question}

Give a clear and simple answer.
"""


    # Generate answer
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    # Display answer
    st.subheader("AI Answer")

    st.write(response["message"]["content"])


    # Show retrieved information
    with st.expander("View Retrieved Document Content"):
        st.write(relevant_text)