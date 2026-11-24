from dataclasses import dataclass

@dataclass(frozen=True)
class Approval:
    action: str
    record_id: str
    reviewer: str

PERMISSIONS = {"student": {"view_status"}, "teacher": {"view_status", "release_result"}}

def handle(actor, action, record_id, approval, audit):
    valid = (
        isinstance(action, str) and isinstance(record_id, str)
        and record_id.startswith("demo-") and len(record_id) > 5
    )
    if not valid:
        outcome = "invalid_request"
    elif action not in PERMISSIONS.get(actor, set()):
        outcome = "denied"
    elif action == "release_result" and approval != Approval(action, record_id, "teacher-reviewer"):
        outcome = "awaiting_review"
    else:
        outcome = "allowed_in_demo"
    audit.append({"actor": actor, "outcome": outcome})
    return outcome

def main():
    audit = []
    approval = Approval("release_result", "demo-42", "teacher-reviewer")
    cases = [
        ("student", "view_status", "demo-42", None, "allowed_in_demo"),
        ("student", "release_result", "demo-42", approval, "denied"),
        ("teacher", "delete_recording", "demo-42", None, "denied"),
        ("teacher", "release_result", "../invalid", None, "invalid_request"),
        ("teacher", "release_result", "demo-43", approval, "awaiting_review"),
        ("teacher", "release_result", "demo-42", approval, "allowed_in_demo"),
    ]
    for actor, action, record_id, review, expected in cases:
        outcome = handle(actor, action, record_id, review, audit)
        assert outcome == expected
        print(actor, action, outcome)
    assert len(audit) == len(cases)
    print("PASS: authorization, approval scope and audit trail")

if __name__ == "__main__":
    main()
