from __future__ import annotations

import math
from itertools import chain, count
from typing import TYPE_CHECKING

from mathlib.lib.exceptions import UnreachableCodeError
from mathlib.numbers import typed_pow

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

SMALL_PRIMES = {
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
}


def sieve(upper_bound: int) -> Iterator[int]:
    """Make an iterator that returns the primes up to upper_bound.

    This method uses the sieve of Eratosthenes to return the
    primes.
    """
    if upper_bound <= 5:  # noqa: PLR2004
        if upper_bound > 2:  # noqa: PLR2004
            yield 2

        if upper_bound > 3:  # noqa: PLR2004
            yield 3

        return

    yield 2

    upper_bound = (upper_bound >> 1) - 1
    indices = [True] * upper_bound
    end_range = int(math.sqrt(upper_bound)) + 1
    for i in range(end_range):
        if indices[i]:
            slice_start = 2 * i * i + 6 * i + 3
            slice_step = 2 * i + 3
            number_of_primes = math.ceil((upper_bound - slice_start) / slice_step)
            indices[slice_start::slice_step] = [False] * number_of_primes

    for i in range(upper_bound):
        if indices[i]:
            yield 2 * i + 3


def _miller_rabin_loop(witness: int, mantissa: int, power: int, n: int) -> bool:
    if pow(witness, mantissa, n) == 1:
        return False

    return all(pow(witness, mantissa * (1 << r), n) + 1 != n for r in range(power))


def _miller_rabin_witnesses(n: int) -> Iterator[int]:
    if n < 2_047:  # noqa: PLR2004
        yield from [2]
        return

    if n < 1_373_653:  # noqa: PLR2004
        yield from [2, 3]
        return

    if n < 9_080_191:  # noqa: PLR2004
        yield from [31, 73]
        return

    if n < 25_326_001:  # noqa: PLR2004
        yield from [2, 3, 5]
        return

    if n < 4_759_123_141:  # noqa: PLR2004
        yield from [2, 7, 61]
        return

    if n < 1_122_004_669_633:  # noqa: PLR2004
        yield from [2, 13, 23, 1662803]
        return

    if n < 2_152_302_898_747:  # noqa: PLR2004
        yield from [2, 3, 5, 7, 11]
        return

    if n < 3_474_749_660_383:  # noqa: PLR2004
        yield from [2, 3, 5, 7, 11, 13]
        return

    if n < 341_550_071_728_321:  # noqa: PLR2004
        yield from [2, 3, 5, 7, 11, 13, 17]
        return

    if n < 3_825_123_056_546_413_051:  # noqa: PLR2004
        yield from [2, 3, 5, 7, 11, 13, 17, 19, 23]
        return

    if n < 318_665_857_834_031_151_167_461:  # noqa: PLR2004
        yield from [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        return

    if n < 3_317_044_064_679_887_385_961_981:  # noqa: PLR2004
        yield from [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        return

    yield from sieve(math.floor(2 * (math.log(n) ** 2)) + 1)


def is_prime(n: int) -> bool:
    """Check if n is a prime number.

    This is a deterministic primality test, but it relies on GHR. This
    seems a good enough compromise. It is very fast for up to 81-bit
    integers, after which it is starts slowing down, due to the fact
    that we need to check for all possible Miller-Rabin witnesses.
    """
    if n < 256:  # noqa: PLR2004
        return n in SMALL_PRIMES

    if n % 2 == 0:
        return False

    mantissa, power = n - 1, 0
    while mantissa & 1 == 0:
        mantissa >>= 1
        power += 1

    return not any(
        _miller_rabin_loop(witness, mantissa, power, n)
        for witness in _miller_rabin_witnesses(n)
    )


def next_prime(n: int) -> int:
    """Get the smallest prime that is larger than n."""
    if n < 2:  # noqa: PLR2004
        return 2

    if n == 2:  # noqa: PLR2004
        return 3

    if n & 1 == 1:
        n += 2
    else:
        n += 1

    for p in count(n, 2):
        if is_prime(p):
            return p

    # A prime will be reached at some point
    raise UnreachableCodeError


def primes() -> Iterator[int]:
    """Make an iterator that returns the prime numbers in ascending order."""
    yield 2

    for n in count(3, 2):  # pragma: no branch
        if is_prime(n):
            yield n


def divisor_sigma(n: int, x: int = 0) -> int:
    """Calculate the sum of the xth powers of the positive divisors of n."""
    out = 1
    for prime_div in chain([2], count(3, 2)):
        power = 1
        while n % prime_div == 0:
            power += 1
            n //= prime_div
        if power != 1:
            if x == 0:
                out *= power
            elif x == 1:
                out *= (typed_pow(prime_div, power) - 1) // (prime_div - 1)
            else:
                prime_div_pow = typed_pow(prime_div, x)
                out *= (typed_pow(prime_div_pow, power) - 1) // (prime_div_pow - 1)
            if n == 1:
                return out

    # At some point divisors will be exhausted
    raise UnreachableCodeError


def factorise(n: int, known_primes: Iterable[int] = ()) -> dict[int, int]:
    if not known_primes:
        known_primes = primes()

    factors = {}
    for prime in known_primes:
        factor = 0
        while n % prime == 0:
            factor += 1
            n //= prime
        if factor:
            factors[prime] = factor
        if n == 1:
            break

    if n != 1:
        missing_factors = factorise(n)
        for factor in factors.keys() | missing_factors.keys():
            factors[factor] = factors.get(factor, 0) + missing_factors.get(factor, 0)

    return factors
