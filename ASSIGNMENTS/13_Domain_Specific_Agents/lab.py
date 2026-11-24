from dataclasses import dataclass
from math import isfinite
from statistics import mean

@dataclass(frozen=True)
class Reading:
    vibration_mm_s: float
    temperature_c: float

def diagnose(readings):
    if len(readings) < 3 or any(
        not isfinite(r.vibration_mm_s) or r.vibration_mm_s < 0 or not isfinite(r.temperature_c)
        for r in readings
    ):
        raise ValueError("Provide at least three valid sensor readings")
    recent = readings[-1]
    baseline = readings[:-1]
    vibration_change = recent.vibration_mm_s - mean(r.vibration_mm_s for r in baseline)
    heat_change = recent.temperature_c - mean(r.temperature_c for r in baseline)
    if recent.vibration_mm_s >= 8 or recent.temperature_c >= 90:
        level, action = "alarm", "Request operator review of the shutdown procedure"
    elif recent.vibration_mm_s >= 5 or recent.temperature_c >= 75 or vibration_change >= 2 or heat_change >= 8:
        level, action = "warning", "Schedule inspection and verify the sensor readings"
    else:
        level, action = "normal", "Continue monitoring"
    return {"condition": level, "vibration_change": round(vibration_change, 1),
            "temperature_change": round(heat_change, 1), "recommendation": action,
            "automatic_shutdown": False}

def main():
    baseline = [Reading(2.5, 62), Reading(3, 64)]
    for last, expected in [
        (Reading(3, 65), "normal"), (Reading(4.8, 72), "warning"), (Reading(8.2, 87), "alarm"),
    ]:
        result = diagnose([*baseline, last])
        print(result)
        assert result["condition"] == expected and result["automatic_shutdown"] is False
    try:
        diagnose([Reading(float("nan"), 50)] * 3)
    except ValueError:
        print("PASS: invalid sensor readings and human-reviewed alarm")
    else:
        raise AssertionError("Expected invalid sensor data to be rejected")

if __name__ == "__main__":
    main()
