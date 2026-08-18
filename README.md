# 📚 Research Paper Question Answering System

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload research papers in PDF format and ask context-aware questions about their content.

The system processes the uploaded document, converts its content into semantic embeddings, retrieves the most relevant information using vector similarity search, and generates answers using a locally hosted **Phi-3 Large Language Model through Ollama**.

The application is built with Python, LangChain, FAISS, Sentence Transformers, Ollama, and Streamlit.

---

## 🚀 Features

* 📄 Upload research papers in PDF format
* 🔍 Extract and process text from PDF documents
* ✂️ Split documents into meaningful text chunks
* 🧠 Generate semantic embeddings using Sentence Transformers
* ⚡ Perform fast similarity search using FAISS
* 🤖 Generate context-aware answers using Phi-3
* 🔒 Run the LLM locally using Ollama
* 💻 Interactive Streamlit web interface
* 📚 Question answering based only on the uploaded document
* 🛠️ Modular RAG pipeline for easier development and maintenance

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │   Upload PDF Paper  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    PDF Processing   │
                    │  Text Extraction    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Text Chunking     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Semantic Embeddings │
                    │ all-MiniLM-L6-v2    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FAISS Index      │
                    │ Vector Similarity   │
                    └──────────┬──────────┘
                               │
                               │ User Question
                               ▼
                    ┌─────────────────────┐
                    │  Query Embedding    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Similarity Search   │
                    │ Relevant Chunks     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Phi-3 via Ollama  │
                    │       LLM           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Final Answer    │
                    └─────────────────────┘
```

---

## 🔄 How the RAG Pipeline Works

The application follows the following workflow:

### 1. PDF Upload

The user uploads a research paper through the Streamlit interface.

### 2. Text Extraction

The application extracts textual content from the uploaded PDF.

### 3. Text Chunking

The extracted text is divided into smaller chunks so that relevant sections can be efficiently retrieved.

### 4. Embedding Generation

Each chunk is converted into a numerical vector using the:

**`all-MiniLM-L6-v2` Sentence Transformer model**

These embeddings represent the semantic meaning of the text.

### 5. Vector Storage

The generated embeddings are indexed using **FAISS (Facebook AI Similarity Search)**.

FAISS enables efficient similarity-based retrieval from the document.

### 6. Question Processing

When the user asks a question, the question is also converted into an embedding.

### 7. Similarity Search

FAISS searches for the most semantically relevant document chunks.

### 8. Context Construction

The retrieved chunks are provided to the language model as context.

### 9. Answer Generation

The local **Phi-3 LLM**, running through Ollama, generates the final answer based on the retrieved document context.

This reduces the likelihood of the model answering from unrelated external knowledge.

---

## 🧰 Tech Stack

| Category             | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| RAG Framework        | LangChain             |
| Embedding Model      | Sentence Transformers |
| Embedding Model Used | all-MiniLM-L6-v2      |
| Vector Database      | FAISS                 |
| Large Language Model | Phi-3                 |
| Local LLM Runtime    | Ollama                |
| Frontend             | Streamlit             |
| Document Format      | PDF                   |
| Version Control      | Git & GitHub          |

---

## 📁 Project Structure

```text
Research-Paper-QA/
│
├── src/
├── sample.pdf
├── app.py
├── test.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The exact contents of `src/` may vary depending on the current implementation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yashagrawal16/Research-Paper-QA.git
```

```bash
cd Research-Paper-QA
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Ollama Setup

This project uses **Ollama** to run the Phi-3 model locally.

Install Ollama and then pull the required model:

```bash
ollama pull phi3
```

Verify that Ollama is running:

```bash
ollama list
```

The application communicates with the locally running Ollama model to generate answers.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Upload a research paper and enter a question related to its content.

---

## 💡 Example Questions

After uploading a research paper, you can ask questions such as:

```text
What is the main objective of this research?

What methodology was used in the study?

What dataset was used?

What are the major findings?

What are the limitations of the proposed approach?

What future improvements were suggested?

Explain the proposed methodology in simple terms.
```

---

## 🧠 Why RAG?

Traditional LLM applications may generate answers using information learned during model training.

RAG improves this workflow by first retrieving relevant information from a specific knowledge source and then providing that information to the LLM.

```text
Traditional LLM

Question
   ↓
LLM
   ↓
Answer


RAG

Question
   ↓
Retriever
   ↓
Relevant Document Chunks
   ↓
LLM + Context
   ↓
Answer
```

For this project, the knowledge source is the **uploaded research paper**.

---

## 🔍 Key Technical Concepts

### Semantic Search

Instead of searching for exact keywords, the system represents both the question and document chunks as vectors and compares their semantic similarity.

### Embeddings

Sentence Transformers converts text into dense numerical representations that capture semantic relationships.

### FAISS

FAISS provides efficient vector similarity search and is used to retrieve the most relevant chunks from the research paper.

### Retrieval-Augmented Generation

RAG combines:

```text
Retrieval + Context + Generation
```

The retriever finds relevant information, while the LLM generates a natural-language response using that information.

### Local LLM

Phi-3 is executed locally through Ollama, avoiding the need to send the research paper's content to a third-party LLM API.

---

## 🔐 Privacy

The project is designed around a local processing workflow.

The research paper is processed locally and the language model is also executed locally through Ollama.

This provides an important advantage when working with research documents that may contain sensitive or unpublished information.

---

## 📈 Future Improvements

Possible improvements to the project include:

* [ ] Add multi-PDF support
* [ ] Add conversation memory
* [ ] Add source/page citations
* [ ] Implement hybrid search using BM25 + vector search
* [ ] Add reranking for better retrieval accuracy
* [ ] Add RAG evaluation using metrics such as Faithfulness and Context Relevance
* [ ] Add document metadata filtering
* [ ] Add OCR support for scanned research papers
* [ ] Add FastAPI backend
* [ ] Dockerize the application
* [ ] Add CI/CD using GitHub Actions
* [ ] Deploy the application
* [ ] Add authentication and user-specific document storage

---

## 🎯 Project Highlights

* Built an **end-to-end RAG pipeline** for research paper question answering.
* Implemented **semantic search** using Sentence Transformer embeddings.
* Used **FAISS vector indexing** for efficient document retrieval.
* Integrated a **local Phi-3 LLM using Ollama**.
* Developed an interactive **Streamlit interface** for PDF upload and question answering.
* Designed the system to generate answers using retrieved document context.

---

## 👨‍💻 Author

**Yash Agrawal**

B.E. Artificial Intelligence & Data Science

GitHub:
https://github.com/yashagrawal16

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub.

**Repository:**
https://github.com/yashagrawal16/Research-Paper-QA
