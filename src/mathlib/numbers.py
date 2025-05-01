from __future__ import annotations

import math
from typing import TYPE_CHECKING, TypeVar, Union, cast

if TYPE_CHECKING:
    from collections.abc import Iterator

T = TypeVar("T", bound=Union[int, float])


def typed_pow(base: T, exponent: int) -> T:
    """Return the value of base raised to the power of exponent.

    Works for both integers and floats.
    """
    if exponent < 0:
        msg = "Exponent must be non-negative"
        raise ValueError(msg)
    return cast("T", base**exponent)


def gcd(*integers: int) -> int:
    """Find the greatest common divisor of the arguments.

    The greatest common divisor of a and 0 is always a, as this
    coincides with gcd to be the greatest lower bound in the
    lattice of divisibility.
    """
    return math.gcd(*integers)


def lcm(*integers: int) -> int:
    """Find the least common multiple of the arguments.

    The least common multiple of a and 0 is always 0, as this
    coincides with lcm to be the least upper bound in the
    lattice of divisibility.
    """
    return math.lcm(*integers)


def isqrt(n: int) -> int:
    """Find the largest integer whose square is less than n."""
    return math.isqrt(n)


def modular_inverse(n: int, mod: int) -> int:
    """Find the modular inverse of n modulo mod."""
    return pow(n, -1, mod)


def fibonacci(n: int, a: int = 1, b: int = 1) -> int:
    """Return the nth Fibonacci number.

    n can be a negative integer as well.
    """
    values = {0: a, 1: b}

    def fib(m: int) -> int:
        if m in values:
            return values[m]

        k = m // 2
        if m & 1 == 1:
            value = fib(k) * (fib(k + 1) + fib(k - 1))
        else:
            value = fib(k) * fib(k) + fib(k - 1) * fib(k - 1)
        values[m] = value
        return value

    if n < 0:
        if n % 2 == 0:
            return -fib(-n)
        return fib(-n)
    return fib(n)


def fibonacci_numbers(a: int = 0, b: int = 1) -> Iterator[int]:
    """Make an iterator that returns the Fibonacci numbers.

    The Fibonacci sequence is configurable, in the sense that the two
    initial values of it can be passed as arguments.
    """
    while True:
        yield a
        a, b = b, a + b


def binomial(n: int, k: int) -> int:
    """Calculate n choose k.

    Calculation is using the multiplicative formula, and is performed
    from the side that will minimise the number of calculations.
    """
    output = 1
    k = min(k, n - k)
    for t in range(k):
        output = (n - t) * output // (t + 1)

    return output


def polygonal_number(s: int, n: int) -> int:
    """Calculate the n-th s-gonal number."""
    return (s - 2) * n * (n - 1) // 2 + n


def pythagorean_triplets(
    upper_bound: int, *, primitive_only: bool = False
) -> Iterator[tuple[int, int, int]]:
    """Make an iterator that yields pythagorean triplets.

    It yields all the pythagorean triplets, that the perimeter
    of the triangle is less than `upper_bound`. Optionally,
    only the primitive ones (ie, the lengths of the sides are
    co-prime) are yielded.
    """
    m = 1
    while 2 * m * (m - 1) <= upper_bound:
        m += 1
        max_n = min(upper_bound // (2 * m) - m + 1, m)
        for n in range(1, max_n):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a, b, c = m**2 - n**2, 2 * m * n, m**2 + n**2
                if primitive_only:
                    yield a, b, c
                else:
                    limit = upper_bound // (2 * m * (m + n))
                    for t in range(1, limit + 1):
                        yield t * a, t * b, t * c
