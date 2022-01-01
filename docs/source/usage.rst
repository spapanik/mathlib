=====
Usage
=====

There are two modules, ``numbers`` and ``primes``.

Numbers
-------

.. py:module:: mathlib.numbers

.. py:function:: gcd(*integers: int) -> int

    Find the greatest common divisor of the arguments.

    The greatest common divisor of a and 0 is always a, as this
    coincides with gcd to be the greatest lower bound in the
    lattice of divisibility.

.. py:function:: lcm(*integers: int) -> int

    Find the least common multiple of the arguments.

    The least common multiple of a and 0 is always 0, as this
    coincides with lcm to be the least upper bound in the
    lattice of divisibility.

.. py:function:: isqrt(n: int) -> int

    Find the largest integer whose square is less than n.

.. py:function:: modular_inverse(n: int, mod: int) -> int

    Find the modular inverse of n modulo mod.

    In python 3.6 and 3.7, the algorithm is based on using
    the Extended Euclid Algorithm, to solve the diophantine
    equation n*x + mod*y = 1.

    In later versions this is just a wrapper over the pow function.

.. py:function:: fibonacci(n: int, a: int = 1, b: int = 1) -> int

    Return the nth Fibonacci number.

    n can be a negative integer as well.

.. py:function:: fibonacci_numbers(a: int = 0, b: int = 1) -> Iterator[int]

    Make an iterator that returns the Fibonacci numbers.

    The Fibonacci sequence is configurable, in the sense that the two
    initial values of it can be passed as arguments.

.. py:function:: binomial(n: int, k: int) -> int

    Calculate n choose k.

    Calculation is using the multiplicative formula, and is performed
    from the side that will minimise the number of calculations.

.. py:function:: polygonal_number(s: int, n: int) -> int

    Calculate the n-th s-gonal number.

Primes
------

.. py:module:: mathlib.primes

.. py:function:: sieve(upper_bound: int) -> Iterator[int]

    Make an iterator that returns the primes up to upper_bound

    This method uses the sieve of Eratosthenes to return the
    primes.

.. py:function:: is_prime(n: int) -> bool

    Check if n is a prime number.

    This is a deterministic primality test, but it relies on GHR. This
    seems a good enough compromise. It is very fast for up to 81-bit
    integers, after which it is starts slowing down, due to the fact
    that we need to check for all possible Miller-Rabin witnesses.

.. py:function:: next_prime(n: int) -> int

    Get the smallest prime that is larger than n.

.. py:function:: primes() -> Iterator[int]

    Make an iterator that returns the prime numbers in ascending order.

.. py:function:: divisor_sigma(n: int, x: int = 0) -> int

    Calculate the sum of the xth powers of the positive divisors of n
