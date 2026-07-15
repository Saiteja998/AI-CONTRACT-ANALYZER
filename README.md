# ⚖️ AI Contract Analyzer

## Overview

**AI Contract Analyzer** is an advanced **Retrieval-Augmented Generation (RAG)** application designed to simplify legal contract analysis using Artificial Intelligence. The system combines **semantic search, vector databases, and Large Language Models (LLMs)** to identify, extract, and analyze important legal clauses from complex contract documents.

Powered by **Groq LLM**, **Sentence Transformer embeddings**, and **ChromaDB**, the application provides accurate clause extraction with confidence scores, source references, and structured JSON responses through an interactive Streamlit interface.

The goal of this project is to make contract review faster, more transparent, and more efficient by reducing manual analysis effort while maintaining traceability of extracted information.

---

# ✨ Key Features

### 📄 Intelligent Document Processing

* Upload and analyze PDF-based contracts
* Extract text efficiently using **PyMuPDF**
* Perform text cleaning and preprocessing for improved retrieval accuracy

### 🧩 Advanced Retrieval Pipeline

* Intelligent document chunking for optimized search
* Semantic similarity search using **ChromaDB**
* Context-aware retrieval powered by **Sentence Transformer embeddings**

### 🤖 AI-Powered Legal Analysis

* Extract important legal clauses using **Groq LLM**
* Identify clause categories and relevant contract sections
* Generate structured and machine-readable JSON responses

### 📊 Transparency & Reliability

* Confidence scoring for extracted information
* Source tracking with page-level references
* Display supporting contract text for verification

### 🌐 Interactive User Experience

* Simple and intuitive **Streamlit web interface**
* Upload documents and receive AI-generated insights instantly

---

# 🏗️ System Architecture

```
                PDF Contract
                     │
                     ▼
          PyMuPDF Text Extraction
                     │
                     ▼
        Text Cleaning & Preprocessing
                     │
                     ▼
          Intelligent Text Chunking
                     │
                     ▼
     Sentence Transformer Embeddings
                     │
                     ▼
          ChromaDB Vector Database
                     │
                     ▼
          Semantic Search Retriever
                     │
                     ▼
              Groq LLM Analysis
                     │
                     ▼
        Structured JSON Response
```

---

# 🛠️ Technology Stack

| Technology            | Purpose                               |
| --------------------- | ------------------------------------- |
| Python                | Core application development          |
| Streamlit             | Interactive web interface             |
| ChromaDB              | Vector database and similarity search |
| Sentence Transformers | Semantic embeddings generation        |
| Groq API              | Large Language Model inference        |
| PyMuPDF               | PDF text extraction                   |
| RAG Architecture      | Context-aware AI document analysis    |

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone <repository-url>
cd AI-Contract-Analyzer
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuration

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

You can use the provided `.env.example` file as a reference.

---

# ▶️ Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

After starting the application, open the local URL displayed in your terminal to access the AI Contract Analyzer interface.

---

# 📌 Sample Output

The application generates structured JSON responses containing:

* Extracted legal clauses
* Clause categories
* Confidence scores
* Source references
* Supporting contract excerpts

### Example Response

```json
{
  "clause": "Termination",
  "category": "Contract Termination",
  "content": "Either party may terminate this agreement with 30 days' written notice.",
  "confidence": 0.96,
  "source": "Page 4"
}
```

---

# 🔮 Future Enhancements

Planned improvements include:

* 📑 Multi-contract comparison and analysis
* 📝 AI-generated contract summaries
* ⚠️ Automated clause risk assessment
* 📊 Advanced legal analytics dashboard
* 📄 PDF report generation
* 🔄 Support for additional document formats
* 📤 Export results to CSV, Excel, and PDF
* 🌍 Multi-language contract analysis

---

# 🎯 Project Impact

AI Contract Analyzer demonstrates how **Generative AI and Retrieval-Augmented Generation** can be applied to real-world legal workflows by improving:

✅ Contract review speed
✅ Information discovery
✅ Legal document transparency
✅ Decision-making efficiency
✅ Traceability of AI-generated insights

---

**AI Contract Analyzer — Transforming Contract Review with Generative AI.**


## Home Page

![Home](assets/home.png)

---


---

## JSON Output

![JSON](assets/json.png)
