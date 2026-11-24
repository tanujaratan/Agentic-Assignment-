import asyncio
import os
import sys
from pathlib import Path
from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.server.fastmcp import FastMCP

NOTES = {"sql-01": "A primary key uniquely identifies a row."}
server = FastMCP("ExamPilot Capstone Fixture")

class NoteResult(TypedDict):
    found: bool
    id: str
    text: str

@server.tool()
def retrieve_note(topic: str) -> NoteResult:
    """Return a course-note passage matching the requested topic."""
    for source_id, passage in NOTES.items():
        if topic.casefold() in passage.casefold():
            return {"found": True, "id": source_id, "text": passage}
    return {"found": False, "id": "", "text": ""}

class ExamState(TypedDict, total=False):
    topic: str
    answer: str
    consent: bool
    events: list[str]
    note: dict
    questions: list[dict]
    valid: bool
    student_view: list[dict]
    score: int
    review: list[str]
    status: str
    trace: list[str]

async def retrieve(state: ExamState):
    params = StdioServerParameters(
        command=sys.executable, args=[str(Path(__file__).resolve()), "--server"],
        env={"PYTHONPATH": os.environ.get("PYTHONPATH", "")},
    )
    with open(os.devnull, "w", encoding="utf8") as errlog:
        async with stdio_client(params, errlog=errlog) as (read, write), ClientSession(read, write) as session:
            await session.initialize()
            response = await session.call_tool("retrieve_note", {"topic": state["topic"]})
            if response.isError:
                raise RuntimeError("MCP retrieval failed")
            note = response.structuredContent
            return {"note": note if note and note["found"] else {}, "trace": ["retrieve_mcp"]}


def generate(state: ExamState):
    note = state["note"]
    questions = [{
        "prompt": "What does a primary key do?",
        "choices": {"A": "Uniquely identifies a row", "B": "Sorts a table"},
        "key": "A", "source": note["id"], "quote": note["text"],
    }] if note else []
    return {"questions": questions, "trace": state["trace"] + ["generate"]}

def validate(state: ExamState):
    note = state["note"]
    questions = state["questions"]
    valid = len(questions) == 1 and all(
        q["source"] == note.get("id") and q["quote"] in note["text"]
        and q["key"] in q["choices"] and len(set(q["choices"].values())) == 2
        for q in questions
    )
    return {"valid": valid, "trace": state["trace"] + ["validate"]}

def reject(state: ExamState):
    return {"status": "rejected", "trace": state["trace"] + ["reject"]}

def deliver(state: ExamState):
    student_view = [{"prompt": q["prompt"], "choices": q["choices"]} for q in state["questions"]]
    return {"student_view": student_view, "trace": state["trace"] + ["deliver"]}

def evaluate(state: ExamState):
    score = sum(q["key"] == state["answer"] for q in state["questions"])
    return {"score": score, "trace": state["trace"] + ["evaluate"]}

def review(state: ExamState):
    events = state.get("events", []) if state.get("consent") else []
    return {"review": events, "status": "complete", "trace": state["trace"] + ["teacher_review"]}

def build_graph():
    graph = StateGraph(ExamState)
    for node in [retrieve, generate, validate, reject, deliver, evaluate, review]:
        graph.add_node(node.__name__, node)
    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", "validate")
    graph.add_conditional_edges("validate",
        lambda state: "deliver" if state["valid"] else "reject",
        {"deliver": "deliver", "reject": "reject"})
    graph.add_edge("reject", END)
    graph.add_edge("deliver", "evaluate")
    graph.add_edge("evaluate", "review")
    graph.add_edge("review", END)
    return graph.compile()

async def demo():
    graph = build_graph()
    fixtures = [
        {"topic": "primary key", "answer": "A", "consent": True,
         "events": ["AI observation: face temporarily out of frame"]},
        {"topic": "primary key", "answer": "B", "consent": False,
         "events": ["Synthetic event supplied without consent"]},
        {"topic": "transactions", "answer": "A", "consent": True, "events": []},
    ]
    first, second, invalid = [await graph.ainvoke(item) for item in fixtures]
    for result in [first, second, invalid]:
        print(result["topic"], result["status"], " → ".join(result["trace"]))
    print("Student payload:", first["student_view"])
    print("Score and teacher review:", first["score"], first["review"])
    assert first["score"] == 1 and first["review"]
    assert set(first["student_view"][0]) == {"prompt", "choices"}
    assert second["score"] == 0 and second["review"] == []
    assert invalid["status"] == "rejected" and "student_view" not in invalid
    print("PASS: grounding gate, answer-key isolation, evaluation and consent")

if __name__ == "__main__":
    if "--server" in sys.argv:
        server.run(transport="stdio")
    else:
        asyncio.run(demo())
