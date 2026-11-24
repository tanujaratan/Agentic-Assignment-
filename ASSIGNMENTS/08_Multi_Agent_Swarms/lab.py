from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

def coverage(question):
    return "join" in question.lower()

def clarity(question):
    return question.endswith("?") and len(question.split()) >= 5

def difficulty(question):
    return "explain" in question.lower()

AGENTS = {"coverage": coverage, "clarity": clarity, "difficulty": difficulty}

def coordinate(question):
    start = Barrier(len(AGENTS))
    def run_check(name):
        start.wait(timeout=5)
        return {"agent": name, "approved": AGENTS[name](question)}
    with ThreadPoolExecutor(max_workers=len(AGENTS)) as pool:
        results = list(pool.map(run_check, AGENTS))
    votes = {result["approved"] for result in results}
    if len(votes) > 1:
        decision = "human_review"
    else:
        decision = "publish" if votes.pop() else "revise"
    return {"trace": ["fan_out", *results, "merge"], "decision": decision}

def main():
    for question, expected in [
        ("Explain how an inner join works?", "publish"),
        ("Is an inner join required?", "human_review"),
        ("Index", "revise"),
    ]:
        result = coordinate(question)
        print(question, result)
        assert result["decision"] == expected
        assert len(result["trace"]) == len(AGENTS) + 2
    print("PASS: parallel rendezvous and disagreement handling")

if __name__ == "__main__":
    main()
