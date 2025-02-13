from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from mathlib import primes
from mathlib.numbers import typed_pow

if TYPE_CHECKING:
    from collections.abc import Iterable


@pytest.mark.parametrize(
    ("upper_bound", "prime_numbers"),
    [
        (2, []),
        (3, [2]),
        (4, [2, 3]),
        (5, [2, 3]),
        (19, [2, 3, 5, 7, 11, 13, 17]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (256, sorted(primes.SMALL_PRIMES)),
    ],
)
def test_sieve(upper_bound: int, prime_numbers: list[int]) -> None:
    assert list(primes.sieve(upper_bound)) == prime_numbers


@pytest.mark.parametrize(
    ("number", "is_prime"),
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (25, False),
        (41, True),
        (97, True),
        (2_133, False),
        (1_234_577, True),
        (1_373_889, False),
        (9_000_011, True),
        (9_080_339, False),
        (21_326_017, True),
        (25_326_215, False),
        (593_441_861, True),
        (4_759_123_151, True),
        (4_759_123_293, False),
        (1_122_004_669_637, True),
        (1_122_004_669_803, False),
        (2_152_302_898_771, True),
        (2_152_302_898_947, False),
        (3_474_749_660_401, True),
        (3_474_749_660_601, False),
        (341_550_071_728_361, True),
        (341_550_071_728_525, False),
        (3_825_123_056_546_413_057, True),
        (3_825_123_056_546_413_239, False),
        (318_665_857_834_031_151_167_483, True),
        (318_665_857_834_031_151_167_663, False),
        (3_317_044_064_679_887_385_962_127, False),
        (33_170_440_646_798_873_859_621_270, False),
    ],
)
def test_is_prime(number: int, is_prime: bool) -> None:
    assert primes.is_prime(number) is is_prime


@pytest.mark.parametrize(
    ("number", "prime"), [(1, 2), (2, 3), (3, 5), (91, 97), (1000, 1009)]
)
def test_next_prime(number: int, prime: int) -> None:
    assert primes.next_prime(number) == prime


def test_primes() -> None:
    prime_numbers = []
    for prime in primes.primes():
        if prime > 30:
            break
        prime_numbers.append(prime)
    assert prime_numbers == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


@pytest.mark.parametrize(
    ("n", "divisors"), [(10, [1, 2, 5, 10]), (12, [1, 2, 3, 4, 6, 12]), (13, [1, 13])]
)
def test_divisor_sigma(n: int, divisors: list[int]) -> None:
    for x in range(5):
        expected = sum(typed_pow(divisor, x) for divisor in divisors)
        assert primes.divisor_sigma(n, x) == expected


@pytest.mark.parametrize(
    ("n", "known_primes", "factors"),
    [
        (10, (2, 3), {2: 1, 5: 1}),
        (12386754, (2,), {2: 1, 3: 2, 83: 1, 8291: 1}),
        (370332963, (2, 3, 5), {3: 2, 7: 1, 11: 2, 13: 1, 37: 1, 101: 1}),
    ],
)
def test_factorise(
    n: int, known_primes: Iterable[int], factors: dict[int, int]
) -> None:
    assert primes.factorise(n) == factors
    assert primes.factorise(n, known_primes) == factors
