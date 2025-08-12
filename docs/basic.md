# Basic

Minimal usage of the math helpers added in this change set.

## Functions

- `multiply(left: int, right: int) -> int`: Returns the product of two integers.
- `divide(left: int, right: int) -> float`: Returns the quotient as a float. Raises `ZeroDivisionError` when `right` is `0`.

## Examples

```py
from cursor_cli_examples import multiply, divide

multiply(4, 3)  # 12
divide(9, 2)    # 4.5
```
