AI Contract Analyzer
Overview

AI Contract Analyzer is a Retrieval-Augmented Generation (RAG) application that analyzes legal contracts by combining semantic search with the Groq LLM. It extracts relevant legal clauses, provides confidence scores, tracks source references, and returns structured JSON responses through an intuitive Streamlit interface.

Features
📄 Upload and analyze PDF contracts
📝 Automatic text extraction and preprocessing
✂️ Intelligent text chunking for efficient retrieval
🔍 Semantic search powered by ChromaDB
🤖 Sentence Transformer embeddings for accurate similarity matching
⚖️ AI-powered legal clause extraction using the Groq LLM
📦 Structured JSON output
📊 Confidence scoring for extracted clauses
📍 Source tracking for transparency and traceability
🌐 Interactive Streamlit web interface
Architecture
PDF Contract
      │
      ▼
 PyMuPDF (Text Extraction)
      │
      ▼
 Text Preprocessing & Chunking
      │
      ▼
 Sentence Transformer Embeddings
      │
      ▼
 ChromaDB Vector Database
      │
      ▼
 Semantic Retriever
      │
      ▼
 Groq LLM
      │
      ▼
 Structured JSON Output
Tech Stack
Python
Streamlit
ChromaDB
Sentence Transformers
Groq API
PyMuPDF
Installation

Clone the repository and install the required dependencies:

pip install -r requirements.txt
Configuration

Create a .env file in the project root and add your Groq API key:

GROQ_API_KEY=your_groq_api_key

You can use the provided .env.example file as a template.

Run the Application

Start the Streamlit application:

streamlit run app.py

Open the local URL displayed in your terminal to access the application.

Sample Output

The application returns structured JSON containing:

Extracted legal clauses
Clause categories
Confidence scores
Source references
Relevant supporting text

Example:

{
  "clause": "Termination",
  "content": "Either party may terminate this agreement with 30 days' written notice.",
  "confidence": 0.96,
  "source": "Page 4"
}
Future Improvements
Multi-contract comparison
AI-generated contract summaries
PDF report generation
Clause risk assessment
Support for multiple document formats
Advanced legal analytics
Export results to CSV, Excel, and PDF

## Home Page

![Home](assets/home.png)

---


---

## JSON Output

![JSON](assets/json.png)
