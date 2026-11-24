# Lab 12 — Safety and Governance

Validate requests, restrict actions by role, require scoped approval and log decisions.

- [Open the notebook](12_safety_governance.ipynb)
- [Python source](lab.py)
- Stack: Python dataclasses and local audit log

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Try valid student access, forbidden release and deletion, an invalid record ID, a mismatched approval and an approved release.

## ExamPilot mapping

Implemented safeguards and partial governance analogue. ExamPilot applies role-aware authorization and answer-key isolation. See backend/app/agents/exam_session_agent/exam_session_agent.py.

## Scope

Roles and approvals are trusted coursework fixtures. Production authorization requires authenticated identity and durable secure audits.
