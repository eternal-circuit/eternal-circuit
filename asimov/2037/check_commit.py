"""Enumerate an abstract effect race between two retries and local revocation."""

from itertools import permutations

EVENTS = ("check_a", "check_b", "revoke", "send_a", "send_b")


def replay(schedule, atomic_endpoint):
    epoch = 0
    committed = 0
    commits_after_revoke = 0
    broker_permits = {}
    for event in schedule:
        if event == "revoke":
            epoch += 1
            continue
        operation, attempt = event.split("_")
        if operation == "check":
            broker_permits[attempt] = epoch == 0 and committed == 0
            continue
        allowed = (epoch == 0 and committed == 0) if atomic_endpoint else (
            broker_permits[attempt]
        )
        if allowed:
            committed += 1
            commits_after_revoke += int(epoch != 0)
    return committed > 1, commits_after_revoke > 0


def main():
    schedules = [
        order for order in permutations(EVENTS)
        if order.index("check_a") < order.index("send_a")
        and order.index("check_b") < order.index("send_b")
    ]
    for atomic_endpoint in (True, False):
        outcomes = [replay(order, atomic_endpoint) for order in schedules]
        duplicates = sum(duplicate for duplicate, _ in outcomes)
        late_commits = sum(late for _, late in outcomes)
        print(f"atomic_endpoint={atomic_endpoint}, schedules={len(schedules)}, "
              f"duplicate={duplicates}, commit_after_revoke={late_commits}")
        if atomic_endpoint and (duplicates or late_commits):
            raise AssertionError("endpoint violated commit invariants")
        if not atomic_endpoint and not (duplicates and late_commits):
            raise AssertionError("split check did not produce both counterexamples")


if __name__ == "__main__":
    main()
