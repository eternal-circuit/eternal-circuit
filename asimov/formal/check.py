"""Independent finite transition model. Run from the repository root."""

from collections import deque
from itertools import product


def successors(x):
    # One representative for each request and health equivalence class.
    for action, error, overshoot, ready in product(
        (-1, 0, 1), (-1, 0, 1), (0, 1), (False, True)
    ):
        y = x + error
        allowed = (ready and action != 0
                   and min(y, y + action) >= 2
                   and max(y, y + action) <= 18)
        if allowed:
            endpoint = x + action
            yield endpoint, min(x, endpoint) - overshoot, max(x, endpoint) + overshoot
        else:
            yield x, x, x


def verify(initial):
    seen = set(initial)
    queue = deque(sorted(seen))
    edges = 0
    while queue:
        x = queue.popleft()
        for endpoint, lo, hi in successors(x):
            edges += 1
            if not 0 <= lo <= endpoint <= hi <= 20:
                raise AssertionError((x, endpoint, lo, hi))
            if endpoint not in seen:
                seen.add(endpoint)
                queue.append(endpoint)
    return seen, edges


if __name__ == "__main__":
    for label, initial in (("demo", {10}), ("all-safe-starts", range(21))):
        states, edges = verify(initial)
        print(f"{label}: states={sorted(states)}, transitions={edges}, violations=0")
