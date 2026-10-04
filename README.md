# Personal Knowledge Base - RAG

An AI-powered document question-answering system that allows users to upload a PDF and ask questions about its content.

## Project Overview

Personal Knowledge Base - RAG uses Retrieval-Augmented Generation (RAG) concepts to retrieve relevant information from a user's document and provide meaningful answers.

Instead of searching the entire document manually, the system extracts the document content, identifies relevant sections, and uses them to answer the user's question.

## Features

- Upload and read PDF documents
- Extract text from PDF files
- Process document content
- Retrieve relevant document information
- Ask questions about the uploaded document
- Generate AI-based answers
- Display retrieved document content
- Simple and user-friendly Streamlit interface
- Local document processing

## Technologies Used

- Python
- Streamlit
- PyPDF
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Retrieval-Augmented Generation (RAG)

## How It Works

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Processing
     ↓
Document Chunking
     ↓
Vector Representation
     ↓
Similarity Search
     ↓
Relevant Document Content
     ↓
AI Answer