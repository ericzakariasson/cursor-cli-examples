# Calculator Web UI

Interactive web interface for the calculator with two modes and a JSON API.

## Run locally

```bash
uv sync
uv run web
# then open http://localhost:5001
```

## Features

- Basic calculator between two numbers
- Chain calculator for multi-step operations
- Uses core functions: `add`, `subtract`, `multiply`, `divide`, `power`

## API

- POST `/api/calculate`
  - Body: `{ "operation": "add|subtract|multiply|divide|power", "left": number, "right": number }`
  - Responses:
    - `200 { "result": number }`
    - `400 { "error": string }` (invalid op, divide by zero, negative exponent)

- POST `/api/chain`
  - Body: `{ "initial": number, "operations": [{ "operation": "add|subtract|multiply|divide|power", "value": number }] }`
  - Responses:
    - `200 { "result": number }`
    - `400 { "error": string }`

## Notes

- Exponent must be a non‑negative integer
- Division by zero returns `400`
- Integers are used when possible for exact results
