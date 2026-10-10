# Task 4.1 - RAG Architecture Notes

## Overview
A question-answering assistant over the documentation of my own Week 1-3
internship projects. Answers are generated only from retrieved text.

    Document -> Chunking -> Embeddings -> FAISS -> Retrieval -> Gemini -> Answer

## 1. Ingestion (`src/ingest.py`)
- Source: 7 Markdown files in `knowledge_base/` (copies of my Week 2-3 task
  READMEs and the root README). The originals were not edited.
- The Offer Letter ID was removed from the knowledge-base copy of the root README.
- Loader: LangChain `TextLoader`.
- Chunking: `RecursiveCharacterTextSplitter`, chunk_size 500, chunk_overlap 50.
  It splits on paragraph breaks first, then lines, then sentences.
- Result: 7 documents -> 64 chunks.

## 2. Embeddings and vector store (`src/build_index.py`)
- Embedding model: `sentence-transformers/all-MiniLM-L6-v2`, run locally.
- Vector store: FAISS (`faiss-cpu`), saved to `faiss_index/` so chunks are not
  re-embedded for every question.
- `faiss_index/` is generated and can be rebuilt with `build_index.py`.

## 3. Retrieval (`src/retrieve.py`)
- The question is embedded with the same model.
- FAISS returns the closest chunks with a distance score (lower = closer).
- `rag.py` retrieves k = 4 chunks.
- Relevance threshold: chunks with distance above 1.2 are dropped. This value
  is a first estimate from a handful of test questions, not a tuned cutoff.

## 4. Generation (`src/rag.py`)
- LLM: `gemini-3.1-flash-lite` via `langchain-google-genai`, temperature 0.
- The prompt tells the model to use only the supplied context, to say
  "I don't know based on the provided documents." if the answer is missing, and
  to say which part is missing if only part of the question is answered.
- If no chunk passes the threshold, the LLM is not called.

## Out-of-scope handling
Two layers: (1) the distance threshold skips the LLM entirely; (2) the prompt
tells the LLM to refuse when the context does not contain the answer.

## Known limitations
- The threshold (1.2) was set from few examples and may need tuning.
- Results sections can rank below less useful chunks (see the test log).
- `audit/audit_notes.md` and other files are not in the knowledge base, so
  details that live only there cannot be answered.
- The free Gemini tier has rate limits and may use inputs to improve Google products.
- `langchain-community` shows a deprecation warning.