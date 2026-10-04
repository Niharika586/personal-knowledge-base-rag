# Personal Knowledge Base - RAG

An AI-powered document question-answering system that allows users to ask questions about their PDF documents.

## Project Overview

Personal Knowledge Base - RAG uses Retrieval-Augmented Generation (RAG) concepts to retrieve relevant information from a document and provide useful answers to user questions.

The application is built using Python and Streamlit.

## Features

- Load PDF documents
- Extract text from PDF files
- Split document text into smaller chunks
- Find relevant information using TF-IDF and cosine similarity
- Ask questions about the document
- Display AI-generated answers
- Show retrieved document content
- Simple and user-friendly Streamlit interface

## Technologies Used

- Python
- Streamlit
- PyPDF
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Natural Language Processing (NLP)
- Retrieval-Augmented Generation (RAG)

## How It Works

```text
PDF Document
     ↓
Text Extraction
     ↓
Text Chunking
     ↓
TF-IDF Vectorization
     ↓
Cosine Similarity
     ↓
Relevant Information Retrieval
     ↓
Question Answering
     ↓
Answer Displayed