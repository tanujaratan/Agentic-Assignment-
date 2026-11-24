from typing import TypedDict

from langgraph.graph import END, START, StateGraph

class ExamState(TypedDict, total=False):
    count: int
    questions: list[str]
    valid: bool
    status: str
    trace: list[str]

def generate(state: ExamState):
    bank = ["What is a primary key?", "What is an inner join?"]
    return {"questions": bank[:max(state["count"], 0)], "trace": ["generate"]}

def validate(state: ExamState):
    valid = state["count"] > 0 and len(state["questions"]) == state["count"]
    return {"valid": valid, "trace": state["trace"] + ["validate"]}

def finish(state: ExamState):
    return {"status": "ready", "trace": state["trace"] + ["finish"]}

def reject(state: ExamState):
    return {"status": "rejected", "questions": [], "trace": state["trace"] + ["reject"]}

def build_graph():
    graph = StateGraph(ExamState)
    for node in [generate, validate, finish, reject]:
        graph.add_node(node.__name__, node)
    graph.add_edge(START, "generate")
    graph.add_edge("generate", "validate")
    graph.add_conditional_edges(
        "validate", lambda state: "ready" if state["valid"] else "invalid",
        {"ready": "finish", "invalid": "reject"},
    )
    graph.add_edge("finish", END)
    graph.add_edge("reject", END)
    return graph.compile()

def main():
    graph = build_graph()
    for count, status in [(2, "ready"), (3, "rejected"), (0, "rejected")]:
        result = graph.invoke({"count": count})
        print(count, result["status"], " → ".join(result["trace"]))
        assert result["status"] == status
        assert bool(result["questions"]) == (status == "ready")
    print("PASS: success and failure routes")

if __name__ == "__main__":
    main()
