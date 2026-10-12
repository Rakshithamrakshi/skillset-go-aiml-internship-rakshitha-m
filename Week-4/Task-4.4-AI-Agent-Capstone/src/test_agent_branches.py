import os

os.environ["LANGSMITH_TRACING"] = "false"  # keep stub runs out of LangSmith

from types import SimpleNamespace

from agent import build_graph
from retrieve import load_vector_store

QUESTION = "By how many points did the Keras spam recall exceed the baseline recall?"


class FakeLLM:
    """Returns a chosen reply for the planning step and a fixed text otherwise."""

    def __init__(self, plan_reply):
        self.plan_reply = plan_reply

    def invoke(self, prompt):
        if "You decide whether a question needs arithmetic" in prompt:
            return SimpleNamespace(text=self.plan_reply)
        return SimpleNamespace(text="STUB ANSWER")


BASE = ["validate_input", "retrieve", "plan_calculation"]
FAIL = BASE + ["calculate", "cannot_verify"]

# (name, what the fake model proposes, expected path)
cases = [
    ("number not in the documents", "0.86 - 7777", FAIL),
    ("division by zero", "0.86 / (0.71 - 0.71)", FAIL),
    ("code injection attempt", "__import__('os').system('echo hi')", FAIL),
    ("prose instead of an expression", "The answer is 0.15", FAIL),
    ("model says NONE", "NONE", BASE + ["generate"]),
    ("valid calculation", "0.86 - 0.71", BASE + ["calculate", "generate"]),
]

store = load_vector_store()
failures = 0
for name, plan_reply, expected in cases:
    result = build_graph(store, FakeLLM(plan_reply)).invoke(
        {"question": QUESTION, "path": []}
    )
    ok = result["path"] == expected
    if name == "valid calculation":
        ok = ok and result.get("calc_result") == 0.15
    print("PASS" if ok else "FAIL", "|", name)
    print("      path:", " -> ".join(result["path"]))
    print("      error:", result.get("calc_error"), "| result:", result.get("calc_result"))
    failures += not ok

print("\nFailures:", failures)