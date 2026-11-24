import json
import math
import re
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory

ALIASES = {"lookup": "search", "lookups": "search", "indexes": "index"}

def embed(text):
    terms = re.findall(r"[a-z]+", text.lower())
    return Counter(ALIASES.get(term, term) for term in terms)

def cosine(left, right):
    divisor = math.sqrt(sum(v*v for v in left.values()) * sum(v*v for v in right.values()))
    return sum(v * right[k] for k, v in left.items()) / divisor if divisor else 0.0

def build_memory(notes, index_path):
    chunks = []
    for doc in sorted(notes.glob("*.txt")):
        for index, line in enumerate(doc.read_text(encoding="utf8").splitlines(), 1):
            if line.strip():
                chunks.append({"id": f"{doc.stem}:{index}", "text": line, "vector": embed(line)})
    index_path.write_text(json.dumps(chunks), encoding="utf8")

def answer(question, memory, index_path):
    memory.append(question)
    query = embed(question)
    chunks = json.loads(index_path.read_text(encoding="utf8"))
    ranked = sorted(chunks, key=lambda chunk: cosine(query, Counter(chunk["vector"])), reverse=True)
    if not ranked or cosine(query, Counter(ranked[0]["vector"])) == 0:
        return "No supporting passage."
    best = ranked[0]
    return f'{best["text"]} [{best["id"]}]'

def main():
    with TemporaryDirectory() as directory:
        notes = Path(directory)
        (notes / "sql.txt").write_text("An index improves search.\nTransactions group changes.", encoding="utf8")
        index = notes / "index.json"
        build_memory(notes, index)
        session = []
        response = answer("indexes lookup", session, index)
        print(response)
        assert "[sql:1]" in response and session == ["indexes lookup"]
        restarted_session = []
        print(answer("transactions", restarted_session, index))
        assert answer("volcano", restarted_session, index) == "No supporting passage."
        assert len(restarted_session) == 2 and len(session) == 1
        print("PASS: session memory, persistent index, source citation and abstention")

if __name__ == "__main__":
    main()
