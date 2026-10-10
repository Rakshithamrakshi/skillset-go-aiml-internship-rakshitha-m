from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Folder that holds our knowledge base files (relative to this script)
KB_DIR = Path(__file__).resolve().parent.parent / "knowledge_base"


def load_documents():
    """Read every .md file in the knowledge_base folder."""
    docs = []
    for path in sorted(KB_DIR.glob("*.md")):
        loader = TextLoader(str(path), encoding="utf-8")
        docs.extend(loader.load())
    return docs


def split_documents(docs, chunk_size=500, chunk_overlap=50):
    """Cut documents into small overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return splitter.split_documents(docs)


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    # Show the first 2 chunks so we can inspect them
    for i, chunk in enumerate(chunks[:2]):
        print(f"\n--- Chunk {i} (from {Path(chunk.metadata['source']).name}) ---")
        print(chunk.page_content)