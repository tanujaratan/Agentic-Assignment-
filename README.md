# Agentic AI Lab Assignments — ExamPilot

This repository contains 14 hands-on Agentic AI lab assignments connected to **ExamPilot**, a proctored examination system. The labs progress from a study-planning agent and tool calling to an integrated exam workflow that retrieves course notes, validates questions, delivers an assessment, scores submissions, and prepares proctoring observations for teacher review.

## Lab Assignments

[Browse all 14 notebooks and their setup instructions](ASSIGNMENTS/README.md).

Each lab folder contains:

- A Jupyter notebook with an explanation, executable code, captured sample output, and validation checks.
- A `lab.py` file that runs the example from the terminal.
- A lab-specific `README.md` explaining how the exercise relates to ExamPilot.

## Getting Started

Use Python 3.11 or newer. From the repository root, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS or Linux: source .venv/bin/activate
python -m pip install -r ASSIGNMENTS/requirements.txt
```

Open a notebook in VS Code or Jupyter, select the Python environment you created, and choose **Run All**. To run the terminal version, open the lab folder and execute `python lab.py`.

## Validation and Scope

All 14 notebooks and their standalone Python scripts were executed and validated. The MCP labs use a real local client/server connection, and the LangGraph labs execute state graphs with success and failure paths. The OpenClaw and cloud operations examples use simulated inputs. The capstone uses synthetic exam and proctoring data. The default lab runs require no API keys.

[View the full ExamPilot project](https://github.com/MICHELLE-HOOLGERI25/ExamPilot-Proctored-Examination-System/tree/feature/ai-vision-proctoring)
