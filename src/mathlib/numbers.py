import math


def lcm(a, b):
    """
    Find the least common multiple of a and b.

    The least common multiple of a and 0 is always 0, as this
    coincides with lcm to be the least upper bound in the
    lattice of divisibility.

    :param a: The first of the numbers to find the lcm
    :param b: The second of the numbers to find the lcm
    :type a: int
    :type b: int
    :return: The least common multiple of a and b
    :rtype: int
    """
    return a * b // math.gcd(a, b)


def fibonacci(n):
    """
    Return the nth Fibonacci number.

    n can be a negative integer as well.

    :param n: the order of the Fibonacci number
    :type n: int
    :return: The nth Fibonacci number
    :rtype: int
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


def fibonacci_numbers(a=0, b=1):
    """
    Make an iterator that returns the Fibonacci numbers.

    The Fibonacci sequence is configurable, in the sense that the two
    initial values of it can be passed as arguments.

    :param a: The first of the two initial values
    :param b: The second of the two initial values
    :type a: int
    :type b: int
    :return: An iterator of the Fibonacci numbers
    :rtype: Iterator[int]
    """
    while True:
        yield a
        a, b = b, a + b
