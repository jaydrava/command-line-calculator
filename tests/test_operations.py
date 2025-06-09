import pytest
from calculator.operation import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 3, 8),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (5, 3, 2),
    (-1, 1, -2),
    (0, 0, 0),
    (100, 200, -100),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (5, 4, 20),
    (-1, 1, -1),
    (0, 5, 0),
    (100, 200, 20000),
])  
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (10, 2, 5),
    (-4, 2, -2),
    (0, 1, 0),
    (100, 20, 5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected
@pytest.mark.parametrize("a, b", [
    (1, 0),
    (5, 0),
    (-1, 0),
    (0, 0),
    (100, 0),
])
def test_divide_by_zero(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

@pytest.mark.parametrize("a, b", [
    (1.5, 2.5),
    (3.1, 4.2),
    (-1.1, 1.1),
    (0.0, 0.0),
    (100.5, 200.5),
])
def test_add_floats(a, b):
    assert add(a, b) == pytest.approx(a + b)
@pytest.mark.parametrize("a, b", [
    (2.5, 1.5),
    (5.3, 3.2),
    (-1.1, 1.1),
    (0.0, 0.0),
    (100.5, 200.5),
])
def test_subtract_floats(a, b):
    assert subtract(a, b) == pytest.approx(a - b)
@pytest.mark.parametrize("a, b", [
    (2.5, 3.5),
    (5.4, 4.3),
    (-1.1, 1.1),
    (0.0, 5.0),
    (100.5, 200.5),
])
def test_multiply_floats(a, b):
    assert multiply(a, b) == pytest.approx(a * b)
@pytest.mark.parametrize("a, b", [
    (6.0, 3.0),
    (10.0, 2.0),
    (-4.0, 2.0),
    (0.0, 1.0),
    (100.5, 20.5),
])
def test_divide_floats(a, b):
    assert divide(a, b) == pytest.approx(a / b)
