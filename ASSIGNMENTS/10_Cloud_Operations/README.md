# Lab 10 — Cloud Operations

Classify a synthetic incident and gate any restart recommendation on approval.

- [Open the notebook](10_cloud_operations_agent.ipynb)
- [Python source](lab.py)
- Stack: Python dataclasses, simulated monitoring

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Compare healthy and degraded metrics. Verify only the designated operator can approve the simulated restart.

## ExamPilot mapping

Partial. ExamPilot has application failures, bounded retries and a separate expiry worker. Automated cloud remediation is outside the supplied project.

## Scope

Health and roles are fixtures. Live monitoring, identity verification, approvals and remediation require a real operations environment.
