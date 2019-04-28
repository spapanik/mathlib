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


@pytest.mark.parametrize(
    ["initial", "count", "expected"],
    [[[0, 7], 4, [0, 7, 7, 14]], [[1, 1], 5, [1, 1, 2, 3, 5]]],
)
def test_fibonacci_numbers(initial, count, expected):
    fibonacci = numbers.fibonacci_numbers(*initial)
    result = list(next(fibonacci) for _ in range(count))
    assert result == expected
