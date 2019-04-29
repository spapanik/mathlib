import pytest

from mathlib import primes


@pytest.mark.parametrize(
    ["upper_bound", "prime_numbers"],
    [
        [2, []],
        [3, [2]],
        [4, [2, 3]],
        [5, [2, 3]],
        [6, [2, 3, 5]],
        [11, [2, 3, 5, 7]],
        [12, [2, 3, 5, 7, 11]],
    ],
)
def test_sieve_two_arguments(upper_bound, prime_numbers):
    assert list(primes.sieve(upper_bound)) == prime_numbers


@pytest.mark.parametrize("number", [2, 3, 5, 41, 97, 593441861])
def test_is_prime(number):
    assert primes.is_prime(number) is True


@pytest.mark.parametrize("number", [1, 4, 6, 25, 3177070365797955661914307])
def test_is_not_prime(number):
    assert primes.is_prime(number) is False


@pytest.mark.parametrize(
    ["number", "prime"], [[1, 2], [2, 3], [3, 5], [91, 97], [1000, 1009]]
)
def test_next_prime(number, prime):
    assert primes.next_prime(number) == prime


def test_primes():
    prime_numbers = []
    for prime in primes.primes():
        if prime > 30:
            break
        prime_numbers.append(prime)
    assert prime_numbers == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
