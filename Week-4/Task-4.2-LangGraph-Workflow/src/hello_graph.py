from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):
    question: str
    cleaned: str
    reply: str


def clean(state: State) -> dict:
    """Node 1: tidy the text."""
    return {"cleaned": state["question"].strip().lower()}


def respond(state: State) -> dict:
    """Node 2: build the reply from the cleaned text."""
    return {"reply": f"I received: {state['cleaned']}"}


builder = StateGraph(State)
builder.add_node("clean", clean)
builder.add_node("respond", respond)
builder.add_edge(START, "clean")
builder.add_edge("clean", "respond")
builder.add_edge("respond", END)
graph = builder.compile()

if __name__ == "__main__":
    result = graph.invoke({"question": "  Hello LangGraph  "})
    print(result)