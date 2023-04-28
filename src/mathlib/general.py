from __future__ import annotations


class Collatz:
    __slots__ = ["_upper_bound", "_steps"]

    def __init__(self, upper_bound: int):
        self._upper_bound = upper_bound
        self._steps = [0] * (upper_bound + 1)
        self._steps[1] = 1

    def __getitem__(self, item: int) -> int:
        if item == 0:
            return 0

        if self._steps[item] == 0:
            self._update_value(item)

        return self._steps[item]

    def _update_value(self, item: int) -> None:
        if self._steps[item] != 0:
            return

        more_steps = 1
        next_key = 3 * item + 1 if item & 1 else item >> 1

        while next_key > self._upper_bound:
            next_key = 3 * next_key + 1 if next_key & 1 else next_key >> 1
            more_steps += 1

        self._update_value(next_key)
        self._steps[item] = self._steps[next_key] + more_steps
