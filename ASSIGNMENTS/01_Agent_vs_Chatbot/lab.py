def chatbot(goal):
    return f"Try breaking '{goal}' into daily study sessions."

def study_planner(topics, daily_minutes, feedback):
    if not topics or daily_minutes <= 0:
        raise ValueError("Provide topics and positive study time")
    goal = "Cover every topic within the daily budget"
    days = ("Monday", "Wednesday", "Friday")
    if len(topics) > len(days):
        raise ValueError("Provide at most three topics")
    plan = {day: (topic, daily_minutes) for day, topic in zip(days, topics)}
    trace = [("Goal", goal), ("Plan", dict(plan)), ("Act", "Draft delivered")]
    unavailable = feedback["unavailable"]
    trace.append(("Observe", f"Unavailable: {unavailable}"))
    if unavailable in plan:
        plan["Saturday"] = plan.pop(unavailable)
    trace.append(("Revise", dict(plan)))
    return plan, trace

def main():
    print("Chatbot:", chatbot("Prepare for a database exam"))
    topics = ["Keys", "Joins", "Indexes"]
    plan, trace = study_planner(topics, 40, {"unavailable": "Wednesday"})
    for stage, result in trace:
        print(f"{stage}: {result}")
    assert plan["Saturday"] == ("Joins", 40) and "Wednesday" not in plan
    assert {topic for topic, _ in plan.values()} == set(topics)
    print("PASS: revision preserves topic coverage")

if __name__ == "__main__":
    main()
