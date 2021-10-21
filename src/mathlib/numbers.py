from typing import Iterator

from mathlib import _seven


def gcd(*integers: int) -> int:
    """
    Find the greatest common divisor of the arguments.

    The greatest common divisor of a and 0 is always a, as this
    coincides with gcd to be the greatest lower bound in the
    lattice of divisibility.
    """
    return _seven.gcd(*integers)


def lcm(*integers: int) -> int:
    """
    Find the least common multiple of the arguments.

    The least common multiple of a and 0 is always 0, as this
    coincides with lcm to be the least upper bound in the
    lattice of divisibility.
    """
    return _seven.lcm(*integers)


def isqrt(n: int) -> int:
    """Find the largest integer whose square is less than n."""
    return _seven.isqrt(n)


def modular_inverse(n: int, mod: int) -> int:
    """
    Find the modular inverse of n modulo mod.

    In python 3.6 and 3.7, the algorithm is based on using
    the Extended Euclid Algorithm, to solve the diophantine
    equation n*x + mod*y = 1.

    In later versions this is just a wrapper over the pow function.
    """
    return _seven.modular_inverse(n, mod)


def fibonacci(n: int, a: int = 1, b: int = 1) -> int:
    """
    Return the nth Fibonacci number.

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
    """
    Make an iterator that returns the Fibonacci numbers.

    The Fibonacci sequence is configurable, in the sense that the two
    initial values of it can be passed as arguments.
    """
    while True:
        yield a
        a, b = b, a + b


def binomial(n: int, k: int) -> int:
    """
    Calculate n choose k.

    Calculation is using the multiplicative formula, and is performed
    from the side that will minimise the number of calculations.
    """
    output = 1
    k = min(k, n - k)
    for t in range(k):
        output = (n - t) * output // (t + 1)

    return output


def polygonal_number(s: int, n: int) -> int:
    """
    Calculate the n-th s-gonal number.
    """

    return (s - 2) * n * (n - 1) // 2 + n
