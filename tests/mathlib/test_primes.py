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


@pytest.mark.parametrize(
    ("number", "prime"), ((1, 2), (2, 3), (3, 5), (91, 97), (1000, 1009))
)
def test_next_prime(number, prime):
    assert primes.next_prime(number) == prime
