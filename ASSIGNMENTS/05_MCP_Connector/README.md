# Lab 05 — MCP Connector

Register, discover and invoke tools through a local MCP stdio connection.

- [Open the notebook](05_mcp_connector.ipynb)
- [Python source](lab.py)
- Stack: Python asyncio, MCP SDK 1.x and FastMCP

## Run

Install the [assignment requirements](../requirements.txt), open this folder, and select **Run All** in the notebook. To run the same example from a terminal, use `python lab.py`.

## Expected checks

Discover the registered tools, list SQL topics, calculate duration for four questions, then send an invalid zero count.

## ExamPilot mapping

Implemented integration. ExamPilot registers exam tools in backend/app/mcp/server.py and invokes them from backend/app/graph/mcp_node.py. This lab uses the MCP 1.x API in its own environment.

## Scope

The server exposes fixture data over a local process. Database access and external transport require additional deployment configuration.
