from __future__ import annotations

import math
from collections.abc import Iterable, Iterator
from itertools import chain, count

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


class UnreachableError(Exception):
    """
    Make mypy happy; this part of the code is unreachable
    """


def sieve(upper_bound: int) -> Iterator[int]:
    """
    Make an iterator that returns the primes up to upper_bound

    This method uses the sieve of Eratosthenes to return the
    primes.
    """
    if upper_bound <= 5:
        if upper_bound > 2:
            yield 2

        if upper_bound > 3:
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
    if n < 2047:
        yield from [2]
        return

    if n < 1373653:
        yield from [2, 3]
        return

    if n < 9080191:
        yield from [31, 73]
        return

    if n < 25326001:
        yield from [2, 3, 5]
        return

    if n < 4759123141:
        yield from [2, 7, 61]
        return

    if n < 1122004669633:
        yield from [2, 13, 23, 1662803]
        return

    if n < 2152302898747:
        yield from [2, 3, 5, 7, 11]
        return

    if n < 3474749660383:
        yield from [2, 3, 5, 7, 11, 13]
        return

    if n < 341550071728321:
        yield from [2, 3, 5, 7, 11, 13, 17]
        return

    if n < 3825123056546413051:
        yield from [2, 3, 5, 7, 11, 13, 17, 19, 23]
        return

    if n < 318665857834031151167461:
        yield from [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        return

    if n < 3317044064679887385961981:
        yield from [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        return

    yield from sieve(math.floor(2 * (math.log(n) ** 2)) + 1)


def is_prime(n: int) -> bool:
    """
    Check if n is a prime number.

    This is a deterministic primality test, but it relies on GHR. This
    seems a good enough compromise. It is very fast for up to 81-bit
    integers, after which it is starts slowing down, due to the fact
    that we need to check for all possible Miller-Rabin witnesses.
    """
    if n < 256:
        return n in SMALL_PRIMES

    if n % 2 == 0:
        return False

    mantissa, power = n - 1, 0
    while mantissa & 1 == 0:
        mantissa >>= 1
        power += 1

    for witness in _miller_rabin_witnesses(n):
        if _miller_rabin_loop(witness, mantissa, power, n):
            return False

    return True


def next_prime(n: int) -> int:
    """
    Get the smallest prime that is larger than n.
    """
    if n < 2:
        return 2

    if n == 2:
        return 3

    if n & 1 == 1:
        n += 2
    else:
        n += 1

    for p in count(n, 2):
        if is_prime(p):
            return p

    msg = "A prime will be reached"
    raise UnreachableError(msg)


def primes() -> Iterator[int]:
    """
    Make an iterator that returns the prime numbers in ascending order.
    """
    yield 2

    for n in count(3, 2):
        if is_prime(n):
            yield n


def divisor_sigma(n: int, x: int = 0) -> int:
    """
    Calculate the sum of the xth powers of the positive divisors of n
    """
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
                out *= (prime_div**power - 1) // (prime_div - 1)
            else:
                out *= (prime_div ** (x * power) - 1) // (prime_div**x - 1)
            if n == 1:
                return out

    msg = "At some point divisors will be exhausted"
    raise UnreachableError(msg)


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
