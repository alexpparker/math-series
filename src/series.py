def fibonacci(n):
    """Returns nth value in the fibonacci series"""
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Returns nth value in the Lucas series"""
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, first = 0, second = 1):
    """Returns nth value for given first and second values"""
    if n == 0:
        return first
    if n == 1:
        return second
    return sum_series(n-1, first, second) + sum_series(n-2, first, second)
