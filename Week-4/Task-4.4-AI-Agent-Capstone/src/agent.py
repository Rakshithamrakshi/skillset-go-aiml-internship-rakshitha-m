import sys
from typing import TypedDict

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, START, StateGraph

from calculator import calculate
from number_check import unsupported_numbers
from rag import MAX_DISTANCE, MODEL_NAME, NO_ANSWER, PROMPT, TOP_K, source_name
from retrieve import load_vector_store, retrieve

INVALID_MESSAGE = "Please type a question with at least 3 characters."
CANNOT_VERIFY = (
    "I found related documents, but I could not verify a calculation "
    "using only numbers that appear in them."
)

PLAN_PROMPT = """You decide whether a question needs arithmetic.

Context:
{context}

Question: {question}

If answering needs adding, subtracting, multiplying or dividing numbers that
appear in the context, reply with ONLY one arithmetic expression that uses
those exact numbers, for example: 0.86 - 0.71
Use only digits, decimal points, + - * / and parentheses. No words, no units,
no percent signs.
If no arithmetic is needed, reply with exactly: NONE"""


class State(TypedDict, total=False):
    question: str
    is_valid: bool
    results: list          # all retrieved chunks with scores
    used: list             # chunks within MAX_DISTANCE
    calc_expression: str   # expression proposed by the model ("" = none)
    calc_result: float     # set only if the tool ran successfully
    calc_error: str        # set if the number check or the tool failed
    answer: str
    path: list             # names of nodes that ran, in order


def add_step(state, name):
    return state.get("path", []) + [name]


def context_text(state):
    """Chunk text with source tags, for the model."""
    return "\n\n---\n\n".join(
        f"[Source: {source_name(doc)}]\n{doc.page_content}" for doc, _ in state["used"]
    )


def chunk_text(state):
    """Chunk text only. File names contain digits (task_2_2), so they must not count."""
    return "\n".join(doc.page_content for doc, _ in state["used"])


def build_graph(store, llm):
    # ---- nodes ----
    def validate_input(state: State) -> dict:
        q = state.get("question")
        ok = isinstance(q, str) and len(q.strip()) >= 3
        return {"is_valid": ok, "path": add_step(state, "validate_input")}

    def retrieve_node(state: State) -> dict:
        results = retrieve(store, state["question"], k=TOP_K)
        used = [(doc, score) for doc, score in results if score <= MAX_DISTANCE]
        return {"results": results, "used": used, "path": add_step(state, "retrieve")}

    def plan_calculation(state: State) -> dict:
        reply = llm.invoke(
            PLAN_PROMPT.format(context=context_text(state), question=state["question"])
        ).text.strip().strip("`").strip()
        expression = "" if reply.upper() == "NONE" else reply
        return {"calc_expression": expression, "path": add_step(state, "plan_calculation")}

    def calculate_node(state: State) -> dict:
        expression = state["calc_expression"]
        try:
            missing = unsupported_numbers(expression, chunk_text(state))
            if missing:
                raise ValueError(f"numbers not found in the documents: {missing}")
            result = round(calculate(expression), 6)
        except ValueError as error:
            return {"calc_error": str(error), "path": add_step(state, "calculate")}
        return {"calc_result": result, "path": add_step(state, "calculate")}

    def generate(state: State) -> dict:
        context = context_text(state)
        if "calc_result" in state:
            context += (
                "\n\n---\n\n[Calculator result, computed exactly] "
                f"{state['calc_expression']} = {state['calc_result']}"
            )
        response = llm.invoke(PROMPT.format(context=context, question=state["question"]))
        return {"answer": response.text, "path": add_step(state, "generate")}

    def invalid_reply(state: State) -> dict:
        return {"answer": INVALID_MESSAGE, "path": add_step(state, "invalid_reply")}

    def no_answer(state: State) -> dict:
        return {"answer": NO_ANSWER, "path": add_step(state, "no_answer")}

    def cannot_verify(state: State) -> dict:
        return {"answer": CANNOT_VERIFY, "path": add_step(state, "cannot_verify")}

    # ---- routers (conditional edges) ----
    def route_after_validate(state: State) -> str:
        return "retrieve" if state["is_valid"] else "invalid_reply"

    def route_after_retrieve(state: State) -> str:
        return "plan_calculation" if state["used"] else "no_answer"

    def route_after_plan(state: State) -> str:
        return "calculate" if state.get("calc_expression") else "generate"

    def route_after_calculate(state: State) -> str:
        return "cannot_verify" if state.get("calc_error") else "generate"

    # ---- wiring ----
    builder = StateGraph(State)
    for name, fn in [
        ("validate_input", validate_input),
        ("retrieve", retrieve_node),
        ("plan_calculation", plan_calculation),
        ("calculate", calculate_node),
        ("generate", generate),
        ("invalid_reply", invalid_reply),
        ("no_answer", no_answer),
        ("cannot_verify", cannot_verify),
    ]:
        builder.add_node(name, fn)

    builder.add_edge(START, "validate_input")
    builder.add_conditional_edges(
        "validate_input", route_after_validate,
        {"retrieve": "retrieve", "invalid_reply": "invalid_reply"},
    )
    builder.add_conditional_edges(
        "retrieve", route_after_retrieve,
        {"plan_calculation": "plan_calculation", "no_answer": "no_answer"},
    )
    builder.add_conditional_edges(
        "plan_calculation", route_after_plan,
        {"calculate": "calculate", "generate": "generate"},
    )
    builder.add_conditional_edges(
        "calculate", route_after_calculate,
        {"generate": "generate", "cannot_verify": "cannot_verify"},
    )
    for end_node in ("generate", "invalid_reply", "no_answer", "cannot_verify"):
        builder.add_edge(end_node, END)
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
    if result.get("calc_expression"):
        print("EXPRESSION:", result["calc_expression"])
        print("RESULT:", result.get("calc_result"), "| ERROR:", result.get("calc_error"))
    print(f"\nANSWER:\n{result['answer']}")