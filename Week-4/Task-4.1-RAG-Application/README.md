# Task 4.1 - RAG Application

## Objective
Build a LangChain RAG pipeline with FAISS that answers questions about my own
internship project documentation, and refuses questions the documents cannot answer.

## Tools Used
- Python 3.11
- LangChain (core, community, text-splitters, huggingface, google-genai)
- FAISS (faiss-cpu)
- sentence-transformers (all-MiniLM-L6-v2)
- Google Gemini (gemini-3.1-flash-lite)

## Work Completed
1. Chose a knowledge base: 7 Markdown files from my Week 2-3 documentation
2. Split them into 64 chunks (size 500, overlap 50)
3. Embedded the chunks locally and stored them in FAISS
4. Inspected retrieved chunks and scores before adding an LLM
5. Added a grounded Gemini prompt and a distance threshold
6. Tested easy, multi-part, near-miss, unanswerable and invalid inputs

## How to Run
```
cd Week-4/Task-4.1-RAG-Application
python -m venv ../../venv-week4
../../venv-week4/Scripts/Activate.ps1
pip install -r requirements.txt
```
Copy `.env.example` to `.env` and add your own Google API key. Then:
```
python src/build_index.py
python src/rag.py "What test accuracy did the CNN get?"
```
`python src/retrieve.py "question"` shows retrieved chunks without calling the LLM.

## Test Results (from my own runs)
| Question | Retrieval | Answer | Result |
|---|---|---|---|
| What test accuracy did the CNN get? | Rank 1 correct chunk (score 0.900) | ~91.6% | Pass |
| Spam recall and precision, and baseline comparison | Rank 1 was a Limitations chunk (0.667); answer was in rank 2 (0.673) | Recall 0.86 / precision 0.88 vs 0.71 / 0.99 | Pass, but poor rank 1 |
| Who won the cricket world cup? | All 4 chunks above 1.2 (1.622-1.741) | "I don't know" (LLM not called) | Pass |
| CNN accuracy on CIFAR-10 | Chunks 1.064-1.131, all passed the threshold | "I don't know" (prompt rule) | Pass |
| Optimizer, batch size and CNN accuracy | Results chunk with "Final configuration" was not retrieved; facts came from another chunk | Adam, 32, 91.64%; noted the sources do not link them | Pass, weak retrieval |
| Problems found auditing the Flask app | Answer was in rank 3 chunk | Four problems | Pass |
| No question given | - | Prompt to type a question | Pass |

## Limitations
See `ARCHITECTURE.md`. In short: the threshold is untuned, some Results chunks
rank poorly, and files outside the knowledge base are not searchable.

## Key Learnings
1. Retrieval and generation fail independently, so inspect chunks first.
2. Duplicate facts across files can hide a retrieval weakness.
3. A distance threshold and a grounded prompt together handle out-of-scope questions.
4. Keys belong in `.env`, never in Git.

## Submission Status
Status: In Progress
Submitted On: