import math
from itertools import count


def _miller_rabin_loop(witness, mantissa, power, n):
    if pow(witness, mantissa, n) == 1:
        return False

    for r in range(power):
        if pow(witness, mantissa * (1 << r), n) + 1 == n:
            return False

    return True


def _miller_rabin_witnesses(n):
    if n < 2047:
        return (2,)

    if n < 1373653:
        return 2, 3

    if n < 9080191:
        return 31, 73

    if n < 25326001:
        return 2, 3, 5

    if n < 4759123141:
        return 2, 7, 61

    if n < 1122004669633:
        return 2, 13, 23, 1662803

    if n < 2152302898747:
        return 2, 3, 5, 7, 11

    if n < 3474749660383:
        return 2, 3, 5, 7, 11, 13

    if n < 341550071728321:
        return 2, 3, 5, 7, 11, 13, 17

    if n < 3825123056546413051:
        return 2, 3, 5, 7, 11, 13, 17, 19, 23

    if n < 318665857834031151167461:
        return 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37

    if n < 3317044064679887385961981:
        return 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41

    return range(2, math.floor(2 * (math.log(n) ** 2)) + 1)


def is_prime(n):
    """
    Check if n is a prime number.

    This is a deterministic primality test, but it relies on GHR. This
    seems a good enough compromise. It is very fast for up to 81-bit
    integers, after which it is starts slowing down, due to the fact
    that we need to check for all possible Miller-Rabin witnesses.

    :param n: the number to be tested for primality
    :type n: int
    :return: True if is a prime number, False otherwise
    :rtype: bool
    """
    if n < 5:
        return n in (2, 3)

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


def next_prime(n):
    """
    Get the smallest prime that is larger than n.

    :param n: the number where we start the search for a prime
    :type n: int
    :return: the smallest prime greater than n
    :rtype: int
    """
    if n < 2:
        return 2

    if n == 2:
        return 3

    if n & 1 == 1:
        n += 2
    else:
        n += 1

    for n in count(n, 2):
        if is_prime(n):
            return n


def primes():
    """
    Make an iterator that returns the prime numbers in ascending order.

    :return: An iterator of the prime numbers
    :rtype: Iterator[int]
    """
    yield 2

    for n in count(3, 2):
        if is_prime(n):
            yield n
