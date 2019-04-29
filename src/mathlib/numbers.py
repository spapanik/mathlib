import math
from typing import Iterator


def lcm(a: int, b: int) -> int:
    """
    Find the least common multiple of a and b.

    The least common multiple of a and 0 is always 0, as this
    coincides with lcm to be the least upper bound in the
    lattice of divisibility.
    """
    return a * b // math.gcd(a, b)


def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number.

    n can be a negative integer as well.
    """
    values = {0: 1, 1: 1}

    def fib(m):
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
        return ((-1) ** (1 - n)) * fib(-n)
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
