from dataclasses import dataclass

@dataclass(frozen=True)
class Metrics:
    healthy: bool
    latency_ms: int
    errors: int
    requests: int

def triage(metrics, logs):
    if metrics.latency_ms < 0 or not 0 <= metrics.errors <= metrics.requests:
        raise ValueError("Invalid monitoring metrics")
    error_rate = metrics.errors / metrics.requests if metrics.requests else 0
    timeouts = sum("DB_TIMEOUT" in line for line in logs)
    degraded = not metrics.healthy or metrics.latency_ms >= 500 or error_rate >= 0.05
    action = "inspect_connection_pool" if timeouts and degraded else "inspect_service"
    return {"incident": degraded, "error_rate": error_rate, "timeout_logs": timeouts,
            "recommendation": action if degraded else "observe"}

def request_restart(report, approved_by=None):
    if not report["incident"]:
        return "not_needed"
    if approved_by != "on_call_operator":
        return "awaiting_operator_approval"
    return "simulated_restart_approved"

def main():
    healthy = triage(Metrics(True, 90, 0, 50), [])
    report = triage(Metrics(False, 725, 8, 50), ["ERROR DB_TIMEOUT", "WARN retry"])
    print("Healthy service:", healthy)
    print("Degraded service:", report)
    assert not healthy["incident"] and request_restart(healthy) == "not_needed"
    assert report["recommendation"] == "inspect_connection_pool"
    for actor in [None, "trainee", "on_call_operator"]:
        print("Simulated decision:", actor, request_restart(report, actor))
    assert request_restart(report, "trainee") == "awaiting_operator_approval"
    assert request_restart(report, "on_call_operator") == "simulated_restart_approved"
    print("PASS: health classification and approval gate")

if __name__ == "__main__":
    main()
