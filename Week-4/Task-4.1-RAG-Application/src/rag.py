import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from retrieve import load_vector_store, retrieve

# Read GOOGLE_API_KEY from the .env file (Git ignores it)
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

MODEL_NAME = "gemini-3.1-flash-lite"
TOP_K = 4            # how many chunks to retrieve
MAX_DISTANCE = 1.2   # chunks farther than this are treated as not relevant
NO_ANSWER = "I don't know based on the provided documents."

PROMPT = """You answer questions about the intern's project documentation.
Use ONLY the context below. Do not use outside knowledge.
If the context does not contain the answer, reply exactly:
I don't know based on the provided documents.
If the context answers only part of the question, answer that part
and say which part is missing.

Context:
{context}

Question: {question}

Answer:"""


def source_name(doc):
    return doc.metadata["source"].replace("\\", "/").split("/")[-1]


def answer_question(store, llm, question):
    """Return (answer, all_results, used_results)."""
    results = retrieve(store, question, k=TOP_K)
    used = [(doc, score) for doc, score in results if score <= MAX_DISTANCE]

    if not used:
        return NO_ANSWER, results, used

    context = "\n\n---\n\n".join(
        f"[Source: {source_name(doc)}]\n{doc.page_content}" for doc, _ in used
    )
    response = llm.invoke(PROMPT.format(context=context, question=question))
    return response.text, results, used


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]).strip()
    if len(question) < 3:
        print("Please type a question, e.g. python rag.py \"What did the CNN score?\"")
        sys.exit(1)

    store = load_vector_store()
    llm = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0)

    answer, results, used = answer_question(store, llm, question)

    print(f"\nQUESTION: {question}")
    print("\nRETRIEVED CHUNKS:")
    for rank, (doc, score) in enumerate(results, start=1):
        status = "USED" if score <= MAX_DISTANCE else "SKIPPED (too far)"
        preview = doc.page_content[:90].replace("\n", " ")
        print(f"  [{rank}] score={score:.3f} | {source_name(doc)} | {status}")
        print(f"      {preview}...")

    print(f"\nANSWER:\n{answer}")