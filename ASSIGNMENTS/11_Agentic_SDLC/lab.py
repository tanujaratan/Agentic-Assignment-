from pathlib import Path
from tempfile import TemporaryDirectory

REQUIREMENT = "Accept positive whole-minute durations and reject floats, booleans and zero."
PLAN = ["validate input", "test accepted and rejected examples", "review", "stage artifact"]
DRAFT = "def valid(minutes):\n    return isinstance(minutes, int) and minutes > 0\n"
REVISION = "def valid(minutes):\n    return type(minutes) is int and minutes > 0\n"

def evaluate(source):
    namespace = {}
    # These are fixed templates defined above, never user or model text.
    exec(compile(source, "<fixed-duration-template>", "exec"), namespace)
    cases = [(15, True), (0, False), (-1, False), (2.5, False), (True, False)]
    return [repr(value) for value, expected in cases if namespace["valid"](value) != expected]

def factory(staging_dir):
    trace = [("requirements", REQUIREMENT), ("plan", PLAN)]
    trace.append(("generate", "fixed first-pass template"))
    failures = evaluate(DRAFT)
    trace.append(("test_feedback", failures))
    if failures != ["True"]:
        raise RuntimeError("Unexpected initial test result")
    trace.append(("revise", "use exact integer type"))
    remaining = evaluate(REVISION)
    trace.append(("retest", remaining))
    if remaining:
        return trace
    trace.append(("review", "fixture checklist passed"))
    staged = staging_dir / "duration_rule.py"
    staged.write_text(REVISION, encoding="utf8")
    trace.append(("local_deploy", staged.name))
    return trace

def main():
    with TemporaryDirectory() as folder:
        staging_dir = Path(folder)
        trace = factory(staging_dir)
        for stage, outcome in trace:
            print(stage, outcome)
        assert trace[-1][0] == "local_deploy"
        assert evaluate((staging_dir / "duration_rule.py").read_text(encoding="utf8")) == []
        print("PASS: test feedback fixed regression and gated staging")

if __name__ == "__main__":
    main()
