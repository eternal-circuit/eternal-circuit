"""Trusted simulation harness. Only request bytes cross its planner interface."""

import argparse
from dataclasses import asdict, dataclass
import json
import sys

from .controller import authorize
from .plant import Axis


@dataclass(frozen=True)
class Faults:
    sensor_bias_mm: int = 0
    sensor_missing: bool = False
    sample_age_ms: int = 0
    ready: bool = True
    excursion_mm: int = 1
    # Trusted test fixture only. This represents invalidated mediation.
    bypass_step_mm: int | None = None


def tick(axis: Axis, frame: bytes, faults: Faults = Faults()) -> dict:
    measured = None if faults.sensor_missing else (
        axis.position_mm + faults.sensor_bias_mm
    )
    authorized, decision = authorize(
        frame, measured, faults.sample_age_ms, faults.ready
    )
    actual = authorized if faults.bypass_step_mm is None else faults.bypass_step_mm
    low, high = axis.stroke(actual, faults.excursion_mm)
    return {
        "request_hex": frame.hex(),
        "sample_mm": measured,
        "decision": decision,
        "authorized_step_mm": authorized,
        "applied_step_mm": actual,
        "settled_mm": axis.position_mm,
        "path_bounds_mm": [low, high],
        "envelope_ok": 0 <= low and high <= 20,
        "fault_inputs": asdict(faults),
    }


def examples():
    axis = Axis()
    for _ in range(11):
        yield "repeated-positive", tick(axis, b"+\n")
    for name, x, frame, faults in (
        ("reverse", 18, b"-\n", Faults()),
        ("missing", 10, b"+\n", Faults(sensor_missing=True)),
        ("stale", 10, b"+\n", Faults(sample_age_ms=6)),
        ("watchdog", 10, b"+\n", Faults(ready=False)),
        ("biased", 20, b"+\n", Faults(sensor_bias_mm=-10)),
        ("excess-excursion", 17, b"+\n", Faults(excursion_mm=4)),
        ("bypass", 20, b"invalid\n", Faults(bypass_step_mm=1)),
    ):
        yield name, tick(Axis(x), frame, faults)


def read_requests(stream):
    """Read bounded records and discard the remainder of oversized lines."""
    while frame := stream.readline(3):
        if not frame.endswith(b"\n"):
            tail = frame
            while tail and not tail.endswith(b"\n"):
                tail = stream.readline(256)
        yield frame


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    axis = Axis()
    records = examples() if args.demo else (
        ("stdin", tick(axis, frame)) for frame in read_requests(sys.stdin.buffer)
    )
    for case, record in records:
        print(json.dumps({"case": case, **record}), flush=True)


if __name__ == "__main__":
    main()
