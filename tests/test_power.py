import pytest

from cursor_cli_examples import power


def test_power_basic():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(7, 1) == 7


def test_power_negative_exponent():
    with pytest.raises(ValueError):
        power(2, -1)


