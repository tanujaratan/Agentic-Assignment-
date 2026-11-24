# Lab 02 — Tool Calling

Select and chain typed Python tools with validation and explicit errors.

- [Open the notebook](02_tool_calling_agent.ipynb)
- [Python source](lab.py)
- Stack: Python standard library

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Use the SQL fixture with valid count, excessive count and an unsupported subject. Compare the returned values and tool traces.

## ExamPilot mapping

Implemented analogue. ExamPilot registers tools for question retrieval, validation, requirements and topics in backend/app/mcp/tools/exam_tools.py.

## Scope

The tool registry, intent rules and question bank are local fixtures.
