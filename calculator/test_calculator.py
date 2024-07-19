# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (0, 5, 5),
    (-3, 5, 2),
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),
    (0, 5, -5),
    (3, -4, 7),
])
def test_subtract(x, y, expected):
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (-3, 5, -15),
])
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (6, 3, 2),
    (8, 4, 2),
    (-6, 3, -2),
])
def test_divide(x, y, expected):
    assert divide(x, y) == expected
