import sys
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

# Reuse the verified Task 4.1 code (Task-4.1 sits next to this folder)
RAG_SRC = Path(__file__).resolve().parents[2] / "Task-4.1-RAG-Application" / "src"
sys.path.insert(0, str(RAG_SRC))

from langchain_google_genai import ChatGoogleGenerativeAI  # noqa: E402
from rag import MAX_DISTANCE, MODEL_NAME, NO_ANSWER, PROMPT, TOP_K, source_name  # noqa: E402
from retrieve import load_vector_store, retrieve  # noqa: E402

INVALID_MESSAGE = "Please type a question with at least 3 characters."


class State(TypedDict, total=False):
    question: str    # raw input
    is_valid: bool   # set by validate_input
    results: list    # set by retrieve: all chunks with scores
    used: list       # set by retrieve: chunks within MAX_DISTANCE
    answer: str      # set by generate / invalid_reply / no_answer
    path: list       # names of nodes that ran, in order


def add_step(state, name):
    return state.get("path", []) + [name]


def build_graph(store, llm):
    # ---- nodes: each reads the state and returns only what it changes ----
    def validate_input(state: State) -> dict:
        q = state.get("question")
        ok = isinstance(q, str) and len(q.strip()) >= 3
        return {"is_valid": ok, "path": add_step(state, "validate_input")}

    def retrieve_node(state: State) -> dict:
        results = retrieve(store, state["question"], k=TOP_K)
        used = [(doc, score) for doc, score in results if score <= MAX_DISTANCE]
        return {"results": results, "used": used,
                "path": add_step(state, "retrieve")}

    def generate(state: State) -> dict:
        context = "\n\n---\n\n".join(
            f"[Source: {source_name(doc)}]\n{doc.page_content}"
            for doc, _ in state["used"]
        )
        response = llm.invoke(
            PROMPT.format(context=context, question=state["question"])
        )
        return {"answer": response.text, "path": add_step(state, "generate")}

    def invalid_reply(state: State) -> dict:
        return {"answer": INVALID_MESSAGE, "path": add_step(state, "invalid_reply")}

    def no_answer(state: State) -> dict:
        return {"answer": NO_ANSWER, "path": add_step(state, "no_answer")}

    # ---- routers: conditional edges, they only return the next node's name ----
    def route_after_validate(state: State) -> str:
        return "retrieve" if state["is_valid"] else "invalid_reply"

    def route_after_retrieve(state: State) -> str:
        return "generate" if state["used"] else "no_answer"

    # ---- wire the graph ----
    builder = StateGraph(State)
    builder.add_node("validate_input", validate_input)
    builder.add_node("retrieve", retrieve_node)
    builder.add_node("generate", generate)
    builder.add_node("invalid_reply", invalid_reply)
    builder.add_node("no_answer", no_answer)

    builder.add_edge(START, "validate_input")
    builder.add_conditional_edges(
        "validate_input",
        route_after_validate,
        {"retrieve": "retrieve", "invalid_reply": "invalid_reply"},
    )
    builder.add_conditional_edges(
        "retrieve",
        route_after_retrieve,
        {"generate": "generate", "no_answer": "no_answer"},
    )
    builder.add_edge("generate", END)
    builder.add_edge("invalid_reply", END)
    builder.add_edge("no_answer", END)
    return builder.compile()


if __name__ == "__main__":
    question = " ".join(sys.argv[1:])
    graph = build_graph(
        load_vector_store(),
        ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0),
    )
    result = graph.invoke({"question": question, "path": []})

    print(f"\nQUESTION: {question!r}")
    print("PATH:", " -> ".join(result["path"]))
    for rank, (doc, score) in enumerate(result.get("results", []), start=1):
        kept = "USED" if score <= MAX_DISTANCE else "SKIPPED"
        print(f"  [{rank}] score={score:.3f} | {source_name(doc)} | {kept}")
    print(f"\nANSWER:\n{result['answer']}")