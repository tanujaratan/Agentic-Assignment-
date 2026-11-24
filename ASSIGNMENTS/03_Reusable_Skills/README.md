# Lab 03 — Reusable Skills

Build a reusable research summary skill with a stable result schema.

- [Open the notebook](03_reusable_skills.ipynb)
- [Python source](lab.py)
- Stack: Python dataclasses

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Reuse the skill with database-index and web-cache passages. Each output follows the same schema and quotes its original source.

## ExamPilot mapping

Partial. ExamPilot separates reusable generation and validation modules, including backend/app/agents/question_generation_agent/question_generation_agent.py. The formal summary skill contract is a lab extension.

## Scope

The sentence splitter and matching are simple lexical rules; general-language summarization needs stronger segmentation and retrieval.
