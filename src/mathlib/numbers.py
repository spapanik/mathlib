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
