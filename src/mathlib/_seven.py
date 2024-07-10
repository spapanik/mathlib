import math
import sys
from functools import reduce

MINOR = sys.version_info.minor


def modular_inverse(n: int, mod: int) -> int:
    return pow(n, -1, mod)


if MINOR >= 9:
    gcd = math.gcd
    lcm = math.lcm
else:

    def gcd(*integers: int) -> int:
        return reduce(math.gcd, integers, 0)

    def lcm(*integers: int) -> int:
        def _lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        return reduce(_lcm, integers, 1)
