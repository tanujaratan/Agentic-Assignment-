# Lab 13 — Discipline-Specific Agents

Use vibration and temperature trends to classify machine conditions and recommend human action.

- [Open the notebook](13_discipline_specific_agents.ipynb)
- [Python source](lab.py)
- Stack: Python statistics and dataclasses

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Compare normal, warning and alarm fixture readings. Verify invalid input handling and that no case automatically shuts down equipment.

## ExamPilot mapping

Domain analogue. ExamPilot applies course-specific assessment and SQL result comparison in backend/app/agents/evaluation_agent/sql_grader.py. Predictive maintenance is the separate disciplinary example.

## Scope

Thresholds are fictional training values. The program never performs a shutdown or controls equipment.
