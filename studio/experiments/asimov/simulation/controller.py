"""Deterministic policy for one settled, indexed axis."""

LOW_MM = 0
HIGH_MM = 20
ERROR_MM = 1
OVERSHOOT_MM = 1
MAX_AGE_MS = 5

REQUESTS = {b"+\n": 1, b"-\n": -1}


def authorize(frame: bytes, measured_mm: int | None, age_ms: int,
              ready: bool) -> tuple[int, str]:
    if not ready:
        return 0, "inhibited"
    if measured_mm is None or not 0 <= age_ms <= MAX_AGE_MS:
        return 0, "invalid-sample"
    step = REQUESTS.get(frame)
    if step is None:
        return 0, "invalid-request"
    uncertainty = ERROR_MM + OVERSHOOT_MM
    if (measured_mm + min(0, step) - uncertainty < LOW_MM
            or measured_mm + max(0, step) + uncertainty > HIGH_MM):
        return 0, "outside-envelope"
    return step, "authorized"
