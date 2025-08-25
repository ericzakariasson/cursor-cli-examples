"""Main module for Cursor CLI examples.

Contains the public API for arithmetic operations and greetings.
"""

from __future__ import annotations
from typing import Callable, Any

__all__ = ["add", "subtract", "multiply", "divide", "power", "hello", "Chain", "pipe"]


def hello() -> str:
    return "Hello world!"


def add(left: int, right: int) -> int:
    """Return the sum of two integers.

    This simple function provides something for tests to exercise.
    """
    return left + right


def subtract(left: int, right: int) -> int:
    """Return the difference of two integers (left minus right)."""
    return left - right


def multiply(left: int, right: int) -> int:
    """Return the product of two integers.

    This complements `add` and `subtract` with a simple multiplicative operation.
    """
    return left * right


def divide(left: int, right: int) -> float:
    """Return the quotient of two integers as a float.

    Raises ZeroDivisionError when right is 0.
    """
    if right == 0:
        raise ZeroDivisionError("division by zero")
    return left / right


def power(base: int, exponent: int) -> int:
    """Return base raised to a non-negative integer exponent.

    Raises ValueError when exponent is negative.
    """
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    return base ** exponent


class Chain:
    """Fluent interface for chaining arithmetic operations.
    
    Example:
        Chain(10).add(5).multiply(2).subtract(3).value()  # Returns 27
    """
    
    def __init__(self, value: int | float):
        """Initialize with a starting value."""
        self._value = value
    
    def add(self, other: int | float) -> Chain:
        """Add a value and return a new Chain."""
        return Chain(add(int(self._value), int(other)) if isinstance(self._value, int) and isinstance(other, int) else self._value + other)
    
    def subtract(self, other: int | float) -> Chain:
        """Subtract a value and return a new Chain."""
        return Chain(subtract(int(self._value), int(other)) if isinstance(self._value, int) and isinstance(other, int) else self._value - other)
    
    def multiply(self, other: int | float) -> Chain:
        """Multiply by a value and return a new Chain."""
        return Chain(multiply(int(self._value), int(other)) if isinstance(self._value, int) and isinstance(other, int) else self._value * other)
    
    def divide(self, other: int | float) -> Chain:
        """Divide by a value and return a new Chain."""
        return Chain(divide(int(self._value), int(other)) if isinstance(self._value, int) and isinstance(other, int) else self._value / other)
    
    def power(self, exponent: int) -> Chain:
        """Raise to a power and return a new Chain."""
        if isinstance(self._value, int):
            return Chain(power(int(self._value), exponent))
        return Chain(self._value ** exponent)
    
    def value(self) -> int | float:
        """Get the final computed value."""
        return self._value
    
    def __str__(self) -> str:
        """String representation showing the current value."""
        return f"Chain({self._value})"
    
    def __repr__(self) -> str:
        """Debug representation."""
        return f"Chain({self._value!r})"


def pipe(initial_value: int | float, *operations: Callable[[Any], Any]) -> int | float:
    """Apply a sequence of operations to an initial value in functional style.
    
    Example:
        pipe(10, lambda x: x + 5, lambda x: x * 2, lambda x: x - 3)  # Returns 27
        
        # Or using partial functions:
        from functools import partial
        pipe(10, partial(add, right=5), partial(multiply, right=2))
    """
    result = initial_value
    for operation in operations:
        result = operation(result)
    return result


