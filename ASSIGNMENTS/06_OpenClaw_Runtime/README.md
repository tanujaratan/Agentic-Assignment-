# Lab 06 — OpenClaw Runtime

Check gateway health before attempting a bounded OpenClaw CLI call.

- [Open the notebook](06_openclaw_runtime.ipynb)
- [Python source](lab.py)
- Stack: Python subprocess, JSON and optional OpenClaw CLI

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Run healthy, timeout, malformed response and unhealthy gateway fixtures. The CLI adapter receives a simulated runner.

## ExamPilot mapping

Implemented optional adapter. Compare the command shapes and error handling in backend/app/openclaw/runtime.py and backend/app/graph/openclaw_node.py.

## Scope

The captured output uses an injected subprocess fixture. The optional live status command requires a locally installed CLI and configured Gateway. The notebook does not invoke a live agent.

## Optional live health check

Run `python lab.py --live-status` with a configured local Gateway. Set `OPENCLAW_EXECUTABLE` in your shell if the CLI is outside your PATH. The command checks Gateway status only. The notebook always uses the simulated fixture.
