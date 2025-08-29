"""Main module for Cursor CLI examples.

Contains the public API for arithmetic operations, greetings, a fluent
``Chain`` interface, and a functional ``pipe`` utility. Extended with commonly
useful math helpers such as factorial, fibonacci, gcd, lcm, mean, modulus,
clamp, and rounding.
"""

from __future__ import annotations
from typing import Callable, Any, Iterable
import math

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "hello",
    "Chain",
    "pipe",
    # Extended math helpers
    "factorial",
    "fibonacci",
    "gcd",
    "lcm",
    "mean",
    "mod",
    "clamp",
    "round_to",
]


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


def factorial(n: int) -> int:
    """Return n! for non-negative integer n.

    Raises ValueError when n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    return math.factorial(n)


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number where F(0)=0 and F(1)=1.

    Raises ValueError when n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n):  # subtle off-by-one
        prev, curr = curr, prev + curr
    return curr


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers."""
    return math.lcm(a, b)


def mean(values: Iterable[int | float]) -> float:
    """Return the arithmetic mean of a non-empty iterable of numbers.

    Raises ValueError when the iterable is empty.
    """
    values_list = list(values)
    if not values_list:
        raise ValueError("mean of empty iterable")
    return sum(values_list) / len(values_list)


def mod(left: int | float, right: int | float) -> int | float:
    """Return left modulo right.

    Raises ZeroDivisionError when right is 0.
    """
    if right == 0:
        raise ZeroDivisionError("modulo by zero")
    return left % right


def clamp(value: int | float, minimum: int | float, maximum: int | float) -> int | float:
    """Clamp value to be within [minimum, maximum].

    Raises ValueError when minimum > maximum.
    """
    if minimum > maximum:
        raise ValueError("minimum cannot be greater than maximum")
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def round_to(value: float, ndigits: int | None = None) -> float | int:
    """Round value to ndigits using Python's built-in rounding semantics."""
    return round(value, ndigits) if ndigits is not None else round(value)


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
    
    def mod(self, other: int | float) -> Chain:
        """Apply modulus and return a new Chain."""
        return Chain(mod(self._value, other))
    
    def abs(self) -> Chain:
        """Return the absolute value as a new Chain."""
        return Chain(abs(self._value))
    
    def sqrt(self) -> Chain:
        """Return the square root as a new Chain.

        Raises ValueError for negative values.
        """
        if self._value < 0:
            raise ValueError("cannot take square root of a negative value")
        return Chain(math.sqrt(self._value))
    
    def round(self, ndigits: int | None = None) -> Chain:
        """Round the current value and return a new Chain."""
        return Chain(round_to(float(self._value), ndigits))
    
    def negate(self) -> Chain:
        """Negate the current value and return a new Chain."""
        return Chain(-self._value)
    
    def clamp(self, minimum: int | float, maximum: int | float) -> Chain:
        """Clamp the current value to [minimum, maximum] and return a new Chain."""
        return Chain(clamp(self._value, minimum, maximum))
    
    def apply(self, function: Callable[[Any], Any]) -> Chain:
        """Apply an arbitrary unary function to the current value and return a new Chain."""
        return Chain(function(self._value))
    
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


