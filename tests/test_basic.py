from cursor_cli_examples import add, hello


def test_hello():
    assert hello() == "Hello world!"


def test_add():
    assert add(2, 3) == 5

