"""Tests for math-series functions."""
import pytest


FIB_PARAMS_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (11, 89),
    (12, 144)
]


@pytest.mark.parametrize("n, result", FIB_PARAMS_TABLE)
def test_fibonacci(n, result):
    """Test Fibonacci function given n"""
    from series import fibonacci
    assert fibonacci(n) == result

LUCAS_PARAMS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29),
    (8, 47),
    (9, 76),
    (10, 123),
    (11, 199),
    (12, 322)
]


@pytest.mark.parametrize("n, result", LUCAS_PARAMS_TABLE)
def test_lucas(n, result):
    """Test lucas function given n"""
    from series import lucas
    assert lucas(n) == result


SUM_PARAMS_TABLE = [
    (0, 0, 1, 0),
    (1, 0, 1, 1),
    (2, 0, 1, 1),
    (3, 0, 1, 2),
    (4, 0, 1, 3),
    (5, 0, 1, 5),
    (6, 0, 1, 8),
    (7, 0, 1, 13),
    (8, 0, 1, 21),
    (9, 0, 1, 34),
    (10, 0, 1, 55),
    (11, 0, 1, 89),
    (12, 0, 1, 144),
    (8, 2, 1, 47),
    (5, 5, 5, 40)
]


@pytest.mark.parametrize("n, first, second, result", SUM_PARAMS_TABLE)
def test_sum(n, first, second, result):
    """Test sum_series function given n, first and second"""
    from series import sum_series
    assert sum_series(n, first, second) == result
