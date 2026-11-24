# ExamPilot Agentic AI Assignments

Fourteen executable Jupyter labs based on the ExamPilot [proctored examination project](https://github.com/MICHELLE-HOOLGERI25/ExamPilot-Proctored-Examination-System/tree/feature/ai-vision-proctoring). Each folder contains one notebook, its Python source, and lab-specific setup and validation notes.

## Setup

From the repository root, create and activate a Python 3.11+ virtual environment, then install the dependencies.

```sh
python -m venv .venv
# Activate in PowerShell: .\.venv\Scripts\Activate.ps1
# Activate in macOS/Linux: source .venv/bin/activate
python -m pip install -r ASSIGNMENTS/requirements.txt
python -m ipykernel install --user --name exampilot-labs --display-name "Python (ExamPilot Labs)"
```

In VS Code, open a notebook and select **Python (ExamPilot Labs)** as its kernel. For a browser interface, optionally install JupyterLab in that environment with `python -m pip install jupyterlab` and launch `jupyter lab`. Open the notebook in its own lab folder and use **Run All**. From a terminal you can also run a lab by opening its folder and using `python lab.py`.

No API keys are needed for the notebooks. Two labs run actual MCP exchanges over local stdio, and two use LangGraph. OpenClaw is simulated by default. Only the optional live status command in Lab 06 requires a configured local Gateway; copy the settings from [the environment example](.env.example) into your shell if the CLI is outside your PATH.

## Notebooks

| Lab | Notebook | Technologies |
| --- | --- | --- |
| 01 | [Agent vs Chatbot](01_Agent_vs_Chatbot/01_agent_vs_chatbot.ipynb) | Python standard library |
| 02 | [Tool Calling](02_Tool_Calling/02_tool_calling_agent.ipynb) | Python standard library |
| 03 | [Reusable Skills](03_Reusable_Skills/03_reusable_skills.ipynb) | Python dataclasses |
| 04 | [Memory and Retrieval](04_Memory_and_Retrieval/04_memory_and_rag.ipynb) | Python JSON, Counter and cosine similarity |
| 05 | [MCP Connector](05_MCP_Connector/05_mcp_connector.ipynb) | Python asyncio, MCP SDK 1.x and FastMCP |
| 06 | [OpenClaw Runtime](06_OpenClaw_Runtime/06_openclaw_runtime.ipynb) | Python subprocess, JSON and optional OpenClaw CLI |
| 07 | [LangGraph Node Graph](07_LangGraph_Node_Graph/07_langgraph_node_graph.ipynb) | Python TypedDict and LangGraph |
| 08 | [Multi-Agent Swarms](08_Multi_Agent_Swarms/08_multi_agent_swarms.ipynb) | Python concurrent.futures and threading |
| 09 | [Deep Research](09_Deep_Research/09_deep_research_agent.ipynb) | Python standard library |
| 10 | [Cloud Operations](10_Cloud_Operations/10_cloud_operations_agent.ipynb) | Python dataclasses, simulated monitoring |
| 11 | [Agentic SDLC Factory](11_Agentic_SDLC/11_agentic_sdlc_factory.ipynb) | Python compile, tempfile and pathlib |
| 12 | [Safety and Governance](12_Safety_and_Governance/12_safety_governance.ipynb) | Python dataclasses and local audit log |
| 13 | [Discipline-Specific Agents](13_Domain_Specific_Agents/13_discipline_specific_agents.ipynb) | Python statistics and dataclasses |
| 14 | [ExamPilot Capstone](14_Capstone_ExamPilot/14_exampilot_capstone.ipynb) | Python asyncio, MCP SDK 1.x and LangGraph |

## Validation

All notebooks were executed in clean Jupyter kernels with the pinned requirements and contain captured output. Tests use synthetic course content, exam activity and monitoring fixtures. The per-lab mappings distinguish implemented ExamPilot paths from proposed extensions.
