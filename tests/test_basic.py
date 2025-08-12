from cursor_cli_examples import add, subtract, multiply, hello


def test_hello():
    assert hello() == "Hello world!"


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12

