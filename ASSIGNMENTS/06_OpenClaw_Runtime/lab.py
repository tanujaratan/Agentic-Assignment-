import argparse
import json
import os
import subprocess

def request(command, runner, timeout=5):
    try:
        result = runner(command, capture_output=True, text=True, timeout=timeout, check=True)
        payload = json.loads(result.stdout)
    except subprocess.TimeoutExpired as error:
        raise RuntimeError("OpenClaw command timed out") from error
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        raise RuntimeError("OpenClaw command failed or returned invalid JSON") from error
    if not isinstance(payload, dict):
        raise RuntimeError("OpenClaw response must be a JSON object")
    return payload

def gateway_status(executable, runner):
    return request([executable, "gateway", "status", "--json"], runner)

def agent_turn(executable, agent, runner):
    if gateway_status(executable, runner).get("rpc", {}).get("ok") is not True:
        raise RuntimeError("Gateway RPC is unhealthy")
    payload = request(
        [executable, "agent", "--agent", agent, "--message",
         "Summarize this fixture: the exam is scheduled for Friday.", "--json"], runner
    )
    if payload.get("ok") is not True:
        raise RuntimeError("Gateway reported an unsuccessful turn")
    return payload

def fixture_runner(command, **options):
    payload = {"rpc": {"ok": True}} if command[1] == "gateway" else {
        "ok": True, "summary": "The exam is scheduled for Friday."
    }
    return subprocess.CompletedProcess(command, 0, stdout=json.dumps(payload))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--live-status", action="store_true", help="Check a configured local Gateway")
    args = parser.parse_args()
    executable = os.getenv("OPENCLAW_EXECUTABLE", "openclaw")
    if args.live_status:
        print("Live Gateway status:", gateway_status(executable, subprocess.run))
        return
    payload = agent_turn(executable, "exam-helper", fixture_runner)
    print("Simulated Gateway and CLI turn:", payload)
    assert payload["summary"].endswith("Friday.")
    def timeout_runner(command, **options):
        raise subprocess.TimeoutExpired(command, options["timeout"])
    def invalid_json_runner(command, **options):
        return subprocess.CompletedProcess(command, 0, stdout="unparseable")
    def unhealthy_runner(command, **options):
        return subprocess.CompletedProcess(command, 0, stdout='{"rpc":{"ok":false}}')
    for runner, expected in [
        (timeout_runner, "timed out"), (invalid_json_runner, "invalid JSON"),
        (unhealthy_runner, "unhealthy"),
    ]:
        try:
            agent_turn(executable, "exam-helper", runner)
        except RuntimeError as error:
            assert expected in str(error)
            print("PASS:", error)
        else:
            raise AssertionError("Expected a handled runtime failure")

if __name__ == "__main__":
    main()
