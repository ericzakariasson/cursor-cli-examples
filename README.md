# cursor-cli-examples

Minimal Python package used to demonstrate Cursor CLI behaviors in CI.

## API
- **hello()**: returns "Hello world!"
- **add(left: int, right: int)**: sum of two integers
- **subtract(left: int, right: int)**: difference of two integers (left minus right)
- **multiply(left: int, right: int)**: product of two integers

### Example
```python
from cursor_cli_examples import multiply

print(multiply(4, 3))  # 12
```
