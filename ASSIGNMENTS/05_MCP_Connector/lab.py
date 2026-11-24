import asyncio
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP

server = FastMCP("ExamPilot Lab Tools")

@server.tool()
def list_topics(subject: str) -> str:
    """List the supported topics of a fixture subject."""
    if subject != "SQL":
        raise ValueError("Unsupported subject")
    return "keys, joins"

@server.tool()
def exam_duration(question_count: int) -> int:
    """Compute the exam duration at two minutes per question."""
    if question_count < 1:
        raise ValueError("At least one question is required")
    return 2 * question_count

async def call_tools():
    params = StdioServerParameters(
        command=sys.executable, args=[str(Path(__file__).resolve()), "--server"],
        env={"PYTHONPATH": os.environ.get("PYTHONPATH", "")},
    )
    with open(os.devnull, "w", encoding="utf8") as errlog:
        async with stdio_client(params, errlog=errlog) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                names = sorted(tool.name for tool in (await session.list_tools()).tools)
                print("Discovered tools:", names)
                assert names == ["exam_duration", "list_topics"]
                for name, payload, expected in [
                    ("list_topics", {"subject": "SQL"}, "keys, joins"),
                    ("exam_duration", {"question_count": 4}, "8"),
                ]:
                    result = await session.call_tool(name, arguments=payload)
                    assert not result.isError and result.content[0].text == expected
                    print(name, "returned", result.content[0].text)
                error = await session.call_tool("exam_duration", arguments={"question_count": 0})
                assert error.isError
                print("PASS: invalid count returned an MCP tool error")


def main():
    if "--server" in sys.argv:
        server.run(transport="stdio")
    else:
        asyncio.run(call_tools())

if __name__ == "__main__":
    main()
