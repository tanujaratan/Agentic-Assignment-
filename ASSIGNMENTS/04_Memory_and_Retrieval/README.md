# Lab 04 — Memory and Retrieval

Separate live session memory from persistent note retrieval and cite the selected passage.

- [Open the notebook](04_memory_and_rag.ipynb)
- [Python source](lab.py)
- Stack: Python JSON, Counter and cosine similarity

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Write two fixture passages into a temporary notes directory. Query using synonyms, start a fresh session, then test an unsupported question.

## ExamPilot mapping

Implemented analogue. ExamPilot carries working state and retrieves scoped notes with a vector store in backend/app/document_processing/vector_store.py and backend/app/schemas/agent_state.py.

## Scope

The sparse vectors approximate meaning through a small hand-written vocabulary. The answer is extractive and the JSON index is local.
