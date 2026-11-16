import io
from itertools import product
import unittest

from asimov.formal.check import successors, verify
from asimov.simulation.controller import authorize
from asimov.simulation.plant import Axis
from asimov.simulation.run import Faults, examples, read_requests, tick


class AuthorizationTests(unittest.TestCase):
    def test_exhaustive_integer_model_agreement(self):
        for x in range(21):
            observed = []
            for request, error, excursion, ready in product(
                (b"-\n", b"bad\n", b"+\n"), (-1, 0, 1),
                (0, 1), (False, True)
            ):
                record = tick(Axis(x), request, Faults(
                    sensor_bias_mm=error, excursion_mm=excursion, ready=ready
                ))
                self.assertTrue(record["envelope_ok"], record)
                observed.append((record["settled_mm"], *record["path_bounds_mm"]))
            self.assertEqual(observed, list(successors(x)))

    def test_reachability(self):
        self.assertEqual(verify({10}), (set(range(1, 20)), 684))
        self.assertEqual(verify(range(21)), (set(range(21)), 756))

    def test_staleness_boundary_and_missing_sample(self):
        for age in (0, 5):
            self.assertEqual(authorize(b"+\n", 10, age, True), (1, "authorized"))
        for age in (-1, 6):
            self.assertEqual(authorize(b"+\n", 10, age, True), (0, "invalid-sample"))
        self.assertEqual(authorize(b"+\n", None, 0, True), (0, "invalid-sample"))

    def test_parser_rejects_oversized_frame_without_reinterpreting_suffix(self):
        frames = list(read_requests(io.BytesIO(b"9" * 1024 + b"+\n-\n+")))
        self.assertEqual(frames, [b"999", b"-\n", b"+"])
        self.assertEqual([authorize(f, 10, 0, True)[0] for f in frames], [0, -1, 0])

    def test_fault_treatment_and_counterexamples(self):
        results = dict(examples())
        for case in ("missing", "stale", "watchdog"):
            self.assertEqual(results[case]["applied_step_mm"], 0)
            self.assertTrue(results[case]["envelope_ok"])
        for case in ("biased", "excess-excursion", "bypass"):
            self.assertFalse(results[case]["envelope_ok"])
        self.assertEqual(results["bypass"]["authorized_step_mm"], 0)


if __name__ == "__main__":
    unittest.main()
