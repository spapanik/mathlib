import pytest

from mathlib.general import Collatz


class TestCollatz:
    @staticmethod
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (1, 4),
            (2, 1),
            (3, 10),
            (4, 2),
            (5, 16),
            (6, 3),
            (7, 22),
            (8, 4),
            (9, 28),
            (10, 5),
            (11, 34),
            (12, 6),
            (13, 40),
            (14, 7),
            (15, 46),
            (16, 8),
            (17, 52),
            (18, 9),
            (19, 58),
            (20, 10),
        ],
    )
    def test_get_next_value(value: int, expected: int) -> None:
        collatz = Collatz()
        assert collatz(value) == expected

    @staticmethod
    @pytest.mark.parametrize(
        ("value", "expected"),
        [
            (1, 1),
            (2, 2),
            (3, 8),
            (4, 3),
            (5, 6),
            (6, 9),
            (7, 17),
            (8, 4),
            (9, 20),
            (10, 7),
            (11, 15),
            (12, 10),
            (13, 10),
            (14, 18),
            (15, 18),
            (16, 5),
            (17, 13),
            (18, 21),
            (19, 21),
            (20, 8),
        ],
    )
    def test_get_steps(value: int, expected: int) -> None:
        collatz = Collatz()
        assert collatz[value] == expected
