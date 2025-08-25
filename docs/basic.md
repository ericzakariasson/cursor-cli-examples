# Basic

## Power

`power(base, exponent)` returns `base` raised to a non‑negative integer `exponent`.

- Negative `exponent` raises `ValueError`.

Example:

```py
from cursor_cli_examples import power

power(2, 3)  # 8
power(5, 0)  # 1
```

## Chain

Fluent method chaining with `Chain` for readable arithmetic:

```py
from cursor_cli_examples import Chain

Chain(10).add(5).multiply(2).subtract(3).value()  # 27
```

## Pipe

Functional composition with `pipe(initial_value, *operations)`:

```py
from cursor_cli_examples import pipe

pipe(10, lambda x: x + 5, lambda x: x * 2, lambda x: x - 3)  # 27
```
