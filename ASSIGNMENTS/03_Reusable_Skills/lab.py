import re
from dataclasses import asdict, dataclass

SKILL_INSTRUCTIONS = "Select up to two sentences relevant to the topic. Quote only the input."
MAX_QUOTED_SENTENCES = 2

@dataclass(frozen=True)
class Summary:
    topic: str
    source: str
    evidence: tuple[str, ...]

def summarize(topic, source, text):
    if not all(field.strip() for field in (topic, source, text)):
        raise ValueError("Topic, source ID and text are required")
    hits = [
        sentence.strip()
        for sentence in re.findall(r"[^.!?]+[.!?]?", text)
        if topic.casefold() in sentence.casefold()
    ]
    return Summary(topic, source, tuple(hits[:MAX_QUOTED_SENTENCES]))

def main():
    cases = [
        ("index", "DB01", "An index can accelerate lookups. Writes can become slower."),
        ("cache", "WEB01", "A cache stores reused responses. A cache has an expiry."),
    ]
    print(SKILL_INSTRUCTIONS)
    for topic, source, text in cases:
        summary = summarize(topic, source, text)
        print(asdict(summary))
        assert 1 <= len(summary.evidence) <= 2
        assert all(quote in text for quote in summary.evidence)
    assert summarize("queue", "DB01", cases[0][2]).evidence == ()
    print("PASS: same schema and grounding rules for two domains")

if __name__ == "__main__":
    main()
