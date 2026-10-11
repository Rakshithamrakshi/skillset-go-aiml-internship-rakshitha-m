# Task 4.3 - LLM Observability with LangSmith

## Objective
Trace the Task 4.2 LangGraph workflow in LangSmith, run a written evaluation
set, record latency and failures, and separate retrieval problems from
generation problems.

## Tools Used
- LangSmith (free Developer plan, project `week4-rag-eval`)
- LangGraph workflow from Task 4.2 and the FAISS index from Task 4.1
- Gemini (gemini-3.1-flash-lite)

## Work Completed
1. Connected the workflow to LangSmith with environment variables (no code changes)
2. Wrote 12 evaluation questions with expected answers before running them
   (`EVAL_QUESTIONS.md`), then added one extra two-part question
3. Ran 13 traced runs and compared each answer with its expectation
4. Opened traces to check retrieved chunks (Q9, Q12 and the two-part run)
5. Wrote the evaluation report (`EVALUATION_REPORT.md`)

## Key Results
Full table, latency and failure analysis: [EVALUATION_REPORT.md](EVALUATION_REPORT.md)
- All 13 runs finished without a crash; no answer contradicted my files.
- Latency: 0.09s to 0.11s when Gemini is skipped; 3.52s to 7.08s when it is called (one run per question).
- Failures found: a Results chunk missing from retrieval (two-part question); the right chunk for Q9 retrieved but dropped by the 1.2 distance limit; a network error outside the traced graph.

## How to Reproduce
Set up Task 4.1 first. Copy `Task-4.1-RAG-Application/.env.example` to `.env`
and fill in your own keys (it lists the LangSmith variables too). Then run
the workflow for any question in `EVAL_QUESTIONS.md`:
```
python Week-4/Task-4.2-LangGraph-Workflow/src/workflow.py "What test accuracy did the CNN get?"
```
Open the project in LangSmith to see the traces.

## Screenshots
In `screenshots/`: the trace list (all 13 runs), a successful trace (Q1),
a blocked trace (Q9), the retrieve output of the two-part run, and the
network-retry terminal output.

## Limitations
- One run per question; no repeated measurements.
- 13 runs is a small set, and groundedness was checked on chunk text only for some of them.
- LangSmith traces expire after 14 days on the free plan, so the screenshots are the permanent record.
- The network retry cause was not investigated.

## Key Learnings
1. A green trace means no crash, not a correct answer.
2. Opening the retrieve step separates "chunk never found" from "chunk found but dropped".
3. Failures that happen before the graph starts do not appear in the trace.
4. A distance limit chosen from a few examples can reject relevant text.

## Submission Status
Status: Completed
Submitted On: 11 Oct 2026