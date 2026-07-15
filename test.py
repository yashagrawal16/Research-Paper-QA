from src.pdf_loader import load_pdf
from src.chunking import split_documents
from src.embeddings import get_embeddings
from src.faiss_store import create_vector_store

# Load PDF
documents = load_pdf("sample.pdf")

# Create chunks
chunks = split_documents(documents)

# Generate embeddings
embeddings = get_embeddings()

# Create vector database
vector_store = create_vector_store(chunks, embeddings)

from src.retriever import get_retriever
from src.llm import get_llm

# Create retriever
retriever = get_retriever(vector_store)

query = "What is Finzi AI?"

results = retriever.invoke(query)

# Combine retrieved chunks
context = "\n\n".join(
    [result.page_content for result in results]
)

prompt = f"""
You are an AI assistant that answers questions ONLY from the provided context.

Context:
{context}

Question:
{query}

Answer:
"""

llm = get_llm()

response = llm.invoke(prompt)

print("\nQUESTION:")
print(query)

print("\nANSWER:")
print(response)

