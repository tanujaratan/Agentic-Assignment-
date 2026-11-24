# Lab 14 — ExamPilot Capstone

Integrate retrieval, generation, validation, exam delivery, scoring and teacher review.

- [Open the notebook](14_exampilot_capstone.ipynb)
- [Python source](lab.py)
- Stack: Python asyncio, MCP SDK 1.x and LangGraph

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Compare a correct answer with consent, a wrong answer without consent and an unsupported topic. Inspect traces, the student payload and the teacher review record.

## ExamPilot mapping

Implemented project components include selected-note retrieval, generation and validation, evaluation persistence and proctoring review. Optional OpenClaw and teacher review have distinct scopes. A concurrent swarm and automated cloud remediation are proposed extensions. See backend/app/graph/exam_graph.py.

## Scope

Questions, timing and proctoring inputs are fixtures. The lab does not open a camera, call Gemini or use the production database. Future work includes persistent attempts and validated observation review.
