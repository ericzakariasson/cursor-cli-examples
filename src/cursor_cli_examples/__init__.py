"""Minimal package for Cursor CLI examples."""

__all__ = ["add", "hello"]

def hello() -> str:
    return "Hello world!"

def add(left: int, right: int) -> int:
    """Return the sum of two integers.

    This simple function provides something for tests to exercise.
    """
    return left + right
