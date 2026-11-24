# Lab 08 — Multi-Agent Swarms

Run independent reviewers concurrently and route conflicts to a human.

- [Open the notebook](08_multi_agent_swarms.ipynb)
- [Python source](lab.py)
- Stack: Python concurrent.futures and threading

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Review three questions that produce unanimous approval, disagreement and unanimous rejection. Look for the fan-out and merge trace.

## ExamPilot mapping

Proposed extension. ExamPilot has specialist generation and validation stages wired sequentially in backend/app/graph/exam_graph.py. This lab runs actual local concurrency separately.

## Scope

The reviewers use fixed rules over local data and share one process. A production swarm would need independent models and failure policies.
