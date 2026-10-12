from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from ingest import load_documents, split_documents

# Where the saved index will live (relative to this script)
INDEX_DIR = Path(__file__).resolve().parent.parent / "faiss_index"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def get_embeddings():
    """Load the local embedding model (downloads ~90 MB the first time)."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def build_index():
    docs = load_documents()
    chunks = split_documents(docs)
    print(f"Embedding {len(chunks)} chunks...")

    embeddings = get_embeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local(str(INDEX_DIR))
    print(f"Saved FAISS index to: {INDEX_DIR}")
    return vector_store


if __name__ == "__main__":
    build_index()