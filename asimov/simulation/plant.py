"""Integer endpoints and an interval enclosing the continuous stroke."""

from dataclasses import dataclass


@dataclass
class Axis:
    position_mm: int = 10

    def stroke(self, step_mm: int, excursion_mm: int) -> tuple[int, int]:
        start = self.position_mm
        self.position_mm += step_mm
        extra = excursion_mm if step_mm else 0
        return (
            min(start, self.position_mm) - extra,
            max(start, self.position_mm) + extra,
        )
