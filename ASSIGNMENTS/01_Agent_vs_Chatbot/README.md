# Lab 01 — Agent vs Chatbot

Compare a one-turn chatbot with a study planner that revises a scheduled plan.

- [Open the notebook](01_agent_vs_chatbot.ipynb)
- [Python source](lab.py)
- Stack: Python standard library

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Use three database topics, 40 minutes per day and feedback that Wednesday is unavailable. The trace shows where the displaced topic goes.

## ExamPilot mapping

Implemented analogue. ExamPilot routes bounded workflow stages with state and traces in backend/app/graph/agentic_loop.py and backend/app/agents/coordinator/coordinator_agent.py. The study planner is a teaching scenario.

## Scope

Runs on fixed days with one feedback item. An actual planner could account for calendars and multiple conflicts.
