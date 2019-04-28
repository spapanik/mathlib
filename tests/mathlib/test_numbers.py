import pytest

from mathlib import numbers


@pytest.mark.parametrize(
    ["n", "expected"],
    (
        (0, 1),
        (1, 1),
        (2, 2),
        (-11, 144),
        (-10, -89),
        (25, 121393),
        (40, 165580141),
    ),
)
def test_fibonacci(n, expected):
    assert numbers.fibonacci(n) == expected
