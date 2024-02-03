from __future__ import annotations


class Collatz:
    __slots__ = ["_steps"]

    def __init__(self) -> None:
        self._steps: dict[int, int] = {1: 1}

    def __call__(self, item: int) -> int:
        return 3 * item + 1 if item & 1 else item >> 1

    def __getitem__(self, item: int) -> int:
        if item <= 0:
            msg = "item must be a positive integer"
            raise ValueError(msg)

        if self._steps.get(item) is None:
            self._update_value(item)

        return self._steps[item]

    def _update_value(self, item: int) -> None:
        if self._steps.get(item):
            return

        next_key = self(item)
        self._update_value(next_key)
        self._steps[item] = self._steps[next_key] + 1
