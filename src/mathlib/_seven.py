import math
import operator
import sys
from functools import reduce

MINOR = sys.version_info.minor


if MINOR >= 8:

    def modular_inverse(n: int, mod: int) -> int:
        return pow(n, -1, mod)

    prod = math.prod
    isqrt = math.isqrt
else:

    def _integer_sqrt(x: int, n: int) -> int:
        return (x + n // x) >> 1

    def isqrt(n: int) -> int:
        if n < 0:
            raise ValueError("isqrt() argument must be nonnegative")

        if n == 0:
            return 0

        initial_guess, next_guess = n, _integer_sqrt(n, n)
        while initial_guess > next_guess:
            initial_guess, next_guess = next_guess, _integer_sqrt(next_guess, n)
        return next_guess

    def prod(iterable, *, start=1):
        return reduce(operator.mul, iterable, start)

    def modular_inverse(n: int, mod: int) -> int:
        original_modulo = mod
        x = 1
        y = 0

        while n > 1:
            x, y = y, x - (n // mod) * y
            n, mod = mod, n % mod

        if x < 0:
            x += original_modulo

        return x


if MINOR >= 9:
    gcd = math.gcd
    lcm = math.lcm
else:

    def gcd(*integers: int) -> int:
        return reduce(math.gcd, integers, 0)

    def lcm(*integers: int) -> int:
        def _lcm(a, b):
            return a * b // gcd(a, b)

        return reduce(_lcm, integers, 1)
