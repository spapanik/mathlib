import pytest

from mathlib import primes


@pytest.mark.parametrize("number", [2, 3, 5, 41, 97, 593441861])
def test_is_prime(number):
    assert primes.is_prime(number) is True


@pytest.mark.parametrize(
    "number", [1, 4, 6, 25, 3177070365797955661914307]
)
def test_is_not_prime(number):
    assert primes.is_prime(number) is False
