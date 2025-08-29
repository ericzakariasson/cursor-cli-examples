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

## Factorial

`factorial(n)` returns `n!` for non‑negative integers.

- Negative `n` raises `ValueError`.

Example:

```py
from cursor_cli_examples import factorial

factorial(5)  # 120
```

## Fibonacci

`fibonacci(n)` returns the n‑th Fibonacci number where F(0)=0 and F(1)=1.

- Negative `n` raises `ValueError`.

Example:

```py
from cursor_cli_examples import fibonacci

fibonacci(5)  # 5
```

## GCD and LCM

`gcd(a, b)` returns the greatest common divisor; `lcm(a, b)` returns the least
common multiple.

Examples:

```py
from cursor_cli_examples import gcd, lcm

gcd(12, 18)  # 6
lcm(6, 8)    # 24
```

## Mean

`mean(values)` returns the arithmetic mean of a non‑empty iterable.

- Empty iterables raise `ValueError`.

Example:

```py
from cursor_cli_examples import mean

mean([1, 2, 3, 4])  # 2.5
```

## Modulus

`mod(left, right)` returns `left % right`.

- `right == 0` raises `ZeroDivisionError`.

Example:

```py
from cursor_cli_examples import mod

mod(10, 3)  # 1
```

## Clamp

`clamp(value, minimum, maximum)` constrains `value` to the inclusive range
`[minimum, maximum]`.

- `minimum > maximum` raises `ValueError`.

Example:

```py
from cursor_cli_examples import clamp

clamp(10, 0, 5)  # 5
```

## Round To

`round_to(value, ndigits=None)` rounds using Python’s built‑in semantics.

Example:

```py
from cursor_cli_examples import round_to

round_to(3.14159, 2)  # 3.14
```
