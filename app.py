import os
import tempfile
import streamlit as st

from src.pdf_loader import load_pdf
from src.chunking import split_documents
from src.embeddings import get_embeddings
from src.faiss_store import create_vector_store
from src.retriever import get_retriever
from src.llm import get_llm

st.set_page_config(
    page_title="Research Paper QA",
    page_icon="📚"
)

st.title("📚 Research Paper Question Answering System")

uploaded_file = st.file_uploader(
    "Upload a Research Paper (PDF)",
    type=["pdf"]
)

question = st.text_input(
    "Ask a question about the paper:"
)

if uploaded_file and question:

    with st.spinner("Processing PDF..."):

        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp_file:

            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        # RAG Pipeline
        documents = load_pdf(pdf_path)
        chunks = split_documents(documents)

        embeddings = get_embeddings()

        vector_store = create_vector_store(
            chunks,
            embeddings
        )

        retriever = get_retriever(vector_store)

        results = retriever.invoke(question)

        context = "\n\n".join(
            [doc.page_content for doc in results]
        )

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY from the context provided.

If the answer is not present in the context, say:
"I could not find the answer in the uploaded paper."

Context:
{context}

Question:
{question}

Answer:
"""

        llm = get_llm()

        response = llm.invoke(prompt)

    st.subheader("Answer")

    st.write(response)