BANK = {"SQL": ("Define a primary key", "Explain an inner join")}

def get_requirements(subject, count):
    if subject not in BANK:
        raise ValueError(f"Unknown subject: {subject}")
    if type(count) is not int or count < 1:
        raise ValueError("Count must be a positive integer")
    return {"subject": subject, "count": count}

def retrieve_questions(subject, count):
    if count > len(BANK[subject]):
        raise ValueError("Question bank has insufficient items")
    return BANK[subject][:count]

def validate_questions(questions):
    return bool(questions) and len(questions) == len(set(questions))

TOOLS = {
    "requirements": get_requirements,
    "retrieve": retrieve_questions,
    "validate": validate_questions,
}

def agent(intent, subject, count):
    trace = []
    try:
        requirements = TOOLS["requirements"](subject, count)
        trace.append("requirements")
        if intent == "inspect":
            return requirements, trace
        if intent != "build":
            raise ValueError("Unknown intent")
        trace.append("retrieve")
        questions = TOOLS["retrieve"](**requirements)
        trace.append("validate")
        if not TOOLS["validate"](questions):
            raise ValueError("Question validation failed")
        return questions, trace
    except ValueError as error:
        return {"error": str(error)}, trace

def main():
    result, trace = agent("build", "SQL", 2)
    print(result, trace)
    assert len(result) == 2 and trace == ["requirements", "retrieve", "validate"]
    for args in [("inspect", "SQL", 1), ("build", "SQL", 3), ("build", "Math", 1)]:
        result, trace = agent(*args)
        print(args, result, trace)
    assert "error" in agent("build", "SQL", 0)[0]
    assert "error" in agent("build", "SQL", 3)[0]
    print("PASS: dispatch, chain and errors")

if __name__ == "__main__":
    main()
