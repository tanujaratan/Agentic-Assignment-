import re

SOURCES = [
    {"id": "N1", "topic": "cache", "dimension": "latency", "finding": "Caching avoids repeated database reads."},
    {"id": "N2", "topic": "cache", "dimension": "freshness", "finding": "Cached records can remain stale until expiry."},
    {"id": "N3", "topic": "index", "dimension": "latency", "finding": "An index can speed up selective queries."},
]

def plan(question):
    tokens = re.findall(r"[a-z]+", question.lower())
    if "cache" in tokens or "caching" in tokens:
        return {"topic": "cache", "dimensions": ("latency", "freshness")}
    if "index" in tokens or "indexes" in tokens:
        return {"topic": "index", "dimensions": ("latency", "freshness")}
    raise ValueError("Choose caching or indexes in the local corpus")

def research(question, sources):
    outline = plan(question)
    report = {"question": question, "evidence": {}, "missing": [], "sources": []}
    for dimension in outline["dimensions"]:
        matches = [
            passage for passage in sources
            if (passage["topic"], passage["dimension"]) == (outline["topic"], dimension)
        ]
        if not matches:
            report["missing"].append(dimension)
            continue
        report["evidence"][dimension] = [
            f'{passage["finding"]} [{passage["id"]}]' for passage in matches
        ]
        report["sources"].extend(passage["id"] for passage in matches)
    return report

def main():
    result = research("How does caching affect latency and freshness?", SOURCES)
    print("Local notes comparison:", result)
    assert set(result["evidence"]) == {"latency", "freshness"}
    assert result["sources"] == ["N1", "N2"]
    result = research("What are the trade-offs of an index?", SOURCES)
    print("Coverage gap:", result)
    assert result["missing"] == ["freshness"]
    print("PASS: citations and evidence gaps")

if __name__ == "__main__":
    main()
