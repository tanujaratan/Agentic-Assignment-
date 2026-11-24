# Lab 07 — LangGraph Node Graph

Build a typed state graph with successful and failed routes.

- [Open the notebook](07_langgraph_node_graph.ipynb)
- [Python source](lab.py)
- Stack: Python TypedDict and LangGraph

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Request two, three and zero questions. Verify the ready and rejected routes and inspect their traces.

## ExamPilot mapping

Implemented analogue. ExamPilot coordinates exam preparation, delivery and evaluation in backend/app/graph/exam_graph.py.

## Scope

Generation uses a fixed bank and validation only checks count; full ExamPilot validates richer constraints.
