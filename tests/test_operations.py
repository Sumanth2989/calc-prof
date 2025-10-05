import pytest
from app.operation import add, subtract, multiply, divide


@pytest.mark.parametrize("a,b,expected", [(0, 0, 0.0), (1, 2, 3.0), (-5, 2.5, -2.5)])
def test_add(a, b, expected):
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a,b,expected", [(5, 2, 3.0), (2, 5, -3.0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a,b,expected", [(3, 4, 12.0), (-3, 4, -12.0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a,b,expected", [(9, 3, 3.0), (7.5, 2.5, 3.0)])
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize("func", [add, subtract, multiply, divide])
@pytest.mark.parametrize("bad", ["x", None, object()])
def test_non_numeric_rejected(func, bad):
    with pytest.raises(TypeError):
        func(bad, 1)
    with pytest.raises(TypeError):
        func(1, bad)
