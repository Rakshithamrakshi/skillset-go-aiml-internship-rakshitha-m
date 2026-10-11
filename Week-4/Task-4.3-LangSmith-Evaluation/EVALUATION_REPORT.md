# Task 4.3 - LangSmith Evaluation Report

## Setup
- Application: the Task 4.2 LangGraph workflow (validate_input, retrieve, generate / invalid_reply / no_answer) over the Task 4.1 FAISS index
- Model: gemini-3.1-flash-lite, free tier. Retrieval: k = 4, distance limit 1.2
- Tracing: LangSmith, project `week4-rag-eval`, 13 traced runs, one run per question
- Expected answers were written before running (`EVAL_QUESTIONS.md`). The last row was added after Task 4.1 testing.

## Evaluation table
| ID | Input | Expected | Actual | Quality | Latency | Failure? | Notes |
|---|---|---|---|---|---|---|---|
| Q1 | CNN test accuracy | ~91.6% | ~91.6% | Correct, complete | 6.70s | No | Chunk text checked in Task 4.1 |
| Q2 | Spam recall/precision and baseline | 0.86/0.88 vs 0.71/0.99 | Same, both parts | Correct, complete | 3.56s | Retrieval weakness | Rank 1 was the Limitations chunk; the numbers were in rank 2 |
| Q3 | Optimizer and batch size | Adam, 32 | Adam, 32 | Correct | 6.50s | No | Rank-1 chunk (Work Completed) has both |
| Q4 | Flask audit problems | Four problems | Four problems | Correct, complete | 6.39s | Retrieval weakness | The list was in the rank-3 chunk |
| Q5 | Final prompt scores | 15/15, 22/22 | 15/15, 22/22 | Correct | 6.16s | No | Chunk text not checked |
| Q6 | Cricket world cup | Refusal | Refusal | Correct | 0.10s | No | Blocked by the distance limit; Gemini not called |
| Q7 | CNN on CIFAR-10 | Refusal | Refusal | Correct | 3.52s | No | Chunks passed the limit (1.064-1.131); the prompt caused the refusal |
| Q8 | `ab` | Asks for 3+ characters | Same | Correct | 0.11s | No | Left at validate_input |
| Q9 | Offer Letter ID | Says the field is blank | "I don't know" | Safe but unhelpful | 0.10s | Yes (partial) | Right chunk at rank 1 scored 1.414 and was dropped by the 1.2 limit |
| Q10 | How did it perform? | Says it is unclear | "I don't know" | Safe, not specific | 0.09s | Partial | All four scores 1.479-1.497; no chunk stands out |
| Q11 | 60-epoch test loss | 0.2807 | 0.2807 | Correct | 7.08s | No | Chunk text not checked |
| Q12 | Number of experiments | 13 | 13 | Correct | 6.41s | Fragile | "13" seen in the rank-4 chunk (1.161) |
| Extra | Optimizer, batch size, CNN accuracy | Adam, 32, 91.64% | Same, with a caveat | Correct; one claim unverified | 5.87s | Retrieval | The "Final configuration" Results chunk was not retrieved |

## Latency
- Runs that skip Gemini (Q6, Q8, Q9, Q10): 0.09s to 0.11s.
- Runs that call Gemini: 3.52s to 7.08s.
- Step times from the traces I opened: Q1 total 6.70s with the Gemini call 6.51s; Q3 total 6.50s with generate 6.38s; Q12 total 6.41s with generate 6.29s. Retrieval took 0.02s to 0.06s.
- One run per question, free tier, so differences of a few seconds between questions are not evidence of anything. The cause of the Gemini time was not investigated.

## Retrieval failures vs generation failures
- Retrieval: the "Final configuration" Results chunk was missing from the top 4 (extra run); Q2 and Q4 had the answer chunk below rank 1; Q9's right chunk was found but removed by the distance limit.
- Generation: no answer contradicted the files I checked. One possible issue: the extra run's answer called the experiments "California Housing dataset experiments", a link I did not verify in the retrieved text.
- Outside the graph: the `ab` run printed five `getaddrinfo failed` retries from huggingface.co before the graph started and then finished using the cached model. LangSmith cannot show this because tracing starts inside the graph. The cause was not investigated.

## What the traces revealed
1. The graph's nodes appear as separate steps, so the branch taken is visible (the Q9 trace has no `generate` step).
2. A green status means no crash, not a correct answer.
3. Reading the `retrieve` output separates "the chunk was never found" from "the chunk was found and dropped".
4. The 1.2 limit was set from a few examples. It rejected a relevant chunk (Q9) and kept a correct answer alive by a small margin (Q12).

## Limitations
- Each question ran once; no repeated measurements.
- Groundedness was checked against chunk text for Q1, Q2, Q3, Q4, Q9 and Q12 only.
- 13 runs is a small evaluation set.
- Traces expire after 14 days on the free plan, so the screenshots are the permanent record.

## What I would improve
- Tune the distance limit with more questions (for example, test 1.1 and 1.5).
- Chunk Results sections so they are not split away from their headings.
- Let Gemini see borderline chunks, so a refusal can explain itself (Q9).

## Evidence
Screenshots are in `screenshots/`: the trace list, a successful trace (Q1), a blocked trace (Q9), the retrieve output of the two-part run, and the network-retry terminal output.