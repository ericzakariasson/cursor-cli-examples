from cursor_cli_examples import add, subtract, multiply, divide, hello, power, Chain, pipe


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


# Chain class tests
def test_chain_basic():
    """Test basic chaining functionality."""
    result = Chain(10).add(5).multiply(2).subtract(3).value()
    assert result == 27  # ((10 + 5) * 2) - 3


def test_chain_single_operation():
    """Test chain with single operation."""
    assert Chain(5).add(3).value() == 8
    assert Chain(10).subtract(4).value() == 6
    assert Chain(6).multiply(7).value() == 42
    assert Chain(15).divide(3).value() == 5.0


def test_chain_power():
    """Test power operation in chain."""
    assert Chain(2).power(3).add(1).value() == 9  # 2^3 + 1


def test_chain_with_floats():
    """Test chain with floating point numbers."""
    result = Chain(10.5).add(2.5).multiply(2).value()
    assert result == 26.0


def test_chain_divide_by_zero():
    """Test that chain propagates division by zero error."""
    import pytest
    with pytest.raises(ZeroDivisionError):
        Chain(10).divide(0).value()


def test_chain_power_negative_exponent():
    """Test that chain propagates power negative exponent error."""
    import pytest
    with pytest.raises(ValueError):
        Chain(2).power(-1).value()


def test_chain_str_repr():
    """Test string representations."""
    chain = Chain(42)
    assert str(chain) == "Chain(42)"
    assert repr(chain) == "Chain(42)"


def test_chain_immutability():
    """Test that chains are immutable - operations return new instances."""
    original = Chain(10)
    new_chain = original.add(5)
    assert original.value() == 10  # Original unchanged
    assert new_chain.value() == 15  # New chain has result


# Pipe function tests
def test_pipe_basic():
    """Test basic pipe functionality."""
    result = pipe(10, lambda x: x + 5, lambda x: x * 2, lambda x: x - 3)
    assert result == 27  # ((10 + 5) * 2) - 3


def test_pipe_single_operation():
    """Test pipe with single operation."""
    result = pipe(5, lambda x: x * 2)
    assert result == 10


def test_pipe_no_operations():
    """Test pipe with no operations returns original value."""
    result = pipe(42)
    assert result == 42


def test_pipe_with_partials():
    """Test pipe with partial functions."""
    from functools import partial
    
    # Create partial functions that fix one argument
    add_5 = partial(lambda x, y: x + y, y=5)
    multiply_2 = partial(lambda x, y: x * y, y=2)
    subtract_3 = partial(lambda x, y: x - y, y=3)
    
    result = pipe(10, add_5, multiply_2, subtract_3)
    assert result == 27


def test_pipe_type_mixing():
    """Test pipe with operations that change types."""
    result = pipe(10, lambda x: x / 2, lambda x: x + 0.5)
    assert result == 5.5


def test_chain_vs_pipe_equivalence():
    """Test that Chain and pipe produce equivalent results."""
    value = 10
    
    # Same computation using both approaches
    chain_result = Chain(value).add(5).multiply(2).subtract(3).value()
    pipe_result = pipe(value, lambda x: x + 5, lambda x: x * 2, lambda x: x - 3)
    
    assert chain_result == pipe_result == 27


