from cursor_cli_examples import add, subtract, multiply, divide, hello, power


def test_hello():
    assert hello() == "Hello world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(9, 2) == 4.5


def test_divide_by_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power_basic():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(7, 1) == 7


def test_power_negative_exponent():
    import pytest
    with pytest.raises(ValueError):
        power(2, -1)


