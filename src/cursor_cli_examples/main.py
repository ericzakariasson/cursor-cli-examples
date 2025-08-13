"""Main module for Cursor CLI examples.

Contains the public API for arithmetic operations and greetings.
"""

from __future__ import annotations

__all__ = ["add", "subtract", "multiply", "divide", "power", "hello"]


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


