"""Deterministic coverage sensitivity for one synthetic remote-maintenance fleet."""

from dataclasses import dataclass
from itertools import combinations


HORIZON = 480
OVERLAY_START = 120
OVERLAY_END = 360
WAIT_LIMIT = 10
MANUAL_MINUTES = 16
OTHER_MINUTES = 12
VALIDATION_MINUTES = 4
REGULAR = (125, 139, 153, 167, 181, 195, 209, 223)
CLUSTERED = (148, 154, 156, 180, 181, 211, 237, 239)
BURST = (125, 126, 127, 128, 129, 130, 131, 132)
OTHER = (50, 120, 147, 173, 206, 237, 280, 380)


@dataclass(frozen=True, order=True)
class Ticket:
    arrival: int
    identity: str
    service: int


@dataclass(frozen=True)
class Outcome:
    max_wait: int
    operator_minutes: int
    last_finish: int

    @property
    def meets_coverage_rule(self):
        return self.max_wait <= WAIT_LIMIT and self.last_finish <= HORIZON


def simulate(family, converted, overlay=False, validation=VALIDATION_MINUTES):
    tickets = [
        Ticket(t, f"family-{i}", validation if i in converted else MANUAL_MINUTES)
        for i, t in enumerate(family)
    ]
    tickets += [Ticket(t, f"other-{i}", OTHER_MINUTES) for i, t in enumerate(OTHER)]

    base_free = 0
    overlay_free = OVERLAY_START
    max_wait = 0
    for ticket in sorted(tickets):
        base_start = max(ticket.arrival, base_free)
        overlay_start = max(ticket.arrival, overlay_free)
        if (overlay and overlay_start < base_start
                and overlay_start + ticket.service <= OVERLAY_END):
            start = overlay_start
            overlay_free = start + ticket.service
        else:
            start = base_start
            base_free = start + ticket.service
        max_wait = max(max_wait, start - ticket.arrival)
    return Outcome(
        max_wait,
        sum(ticket.service for ticket in tickets),
        max(base_free, overlay_free if overlay else 0),
    )


def coverage_by_conversion_count(family):
    """Each subset appears once. The counts carry no probability measure."""
    for count in range(len(family) + 1):
        outcomes = [
            simulate(family, converted)
            for converted in combinations(range(len(family)), count)
        ]
        waits = [outcome.max_wait for outcome in outcomes]
        passes = sum(outcome.meets_coverage_rule for outcome in outcomes)
        yield count, min(waits), max(waits), passes, len(outcomes)


def verify():
    all_converted = set(range(len(REGULAR)))
    assert simulate(REGULAR, set()) == Outcome(59, 224, 392)
    assert simulate(REGULAR, set(), overlay=True) == Outcome(2, 224, 392)
    assert simulate(REGULAR, all_converted) == Outcome(9, 128, 392)
    assert simulate(CLUSTERED, set(), overlay=True) == Outcome(10, 224, 392)
    assert simulate(CLUSTERED, all_converted) == Outcome(14, 128, 392)
    assert simulate(CLUSTERED, all_converted, overlay=True) == Outcome(3, 128, 392)
    assert simulate(BURST, all_converted) == Outcome(28, 128, 392)
    assert simulate(BURST, all_converted, overlay=True) == Outcome(9, 128, 392)
    assert list(coverage_by_conversion_count(REGULAR))[-3:] == [
        (6, 9, 23, 2, 28), (7, 9, 14, 3, 8), (8, 9, 9, 1, 1)
    ]
    assert simulate(REGULAR, all_converted, validation=8).meets_coverage_rule
    assert not simulate(REGULAR, all_converted, validation=9).meets_coverage_rule


def main():
    verify()
    all_converted = set(range(len(REGULAR)))
    print("trace, conversions, overlay, max wait (min), operator-min, passes")
    for name, family in (("regular", REGULAR), ("clustered", CLUSTERED),
                         ("burst", BURST)):
        for converted in (set(), all_converted):
            for overlay in (False, True):
                outcome = simulate(family, converted, overlay)
                print(name, len(converted), overlay, outcome.max_wait,
                      outcome.operator_minutes, outcome.meets_coverage_rule)
    print("\nregular conversions, minimum wait, maximum wait, passing subsets, subsets")
    for row in coverage_by_conversion_count(REGULAR):
        print(*row)
    print("\nvalidation minutes, one-tech max wait (regular, clustered, burst)")
    for duration in (1, 2, 4, 8, 9, 12, 16):
        print(duration, *(simulate(family, all_converted, validation=duration).max_wait
                          for family in (REGULAR, CLUSTERED, BURST)))


if __name__ == "__main__":
    main()
