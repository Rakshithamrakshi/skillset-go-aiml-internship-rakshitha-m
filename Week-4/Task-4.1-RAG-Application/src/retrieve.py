import sys

from langchain_community.vectorstores import FAISS

from build_index import INDEX_DIR, get_embeddings


def load_vector_store():
    """Load the saved FAISS index from disk (no re-embedding of chunks)."""
    return FAISS.load_local(
        str(INDEX_DIR),
        get_embeddings(),
        allow_dangerous_deserialization=True,
    )


def retrieve(vector_store, question, k=3):
    """Return the k closest chunks, each with a distance score."""
    return vector_store.similarity_search_with_score(question, k=k)


def show_results(question, results):
    print(f"\nQUESTION: {question}")
    for rank, (doc, score) in enumerate(results, start=1):
        source = doc.metadata["source"].replace("\\", "/").split("/")[-1]
        print(f"\n[{rank}] score={score:.3f} | source={source}")
        print(doc.page_content)


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "What test accuracy did the CNN get?"
    store = load_vector_store()
    show_results(question, retrieve(store, question))