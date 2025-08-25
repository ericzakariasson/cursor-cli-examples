# Cursor CLI Examples

Cursor CLI subagents and GitHub Actions.

## Subagents

Spawn parallel AI agents for any task:

```bash
cursor-agent -p "Research patterns" --model gpt-5 --force
cursor-agent -p "Implement features" --model sonnet-4 --force
cursor-agent -p "Debug code" --model auto --force
```

## Autonomous workflows

Workflows handle repository maintenance automatically:

- Fix CI failures
- Resolve merge conflicts
- Improve PR descriptions
- Security audits
- Translate i18n keys
- Update documentation

## Usage

```bash
uv sync && uv run pytest
python -c "from cursor_cli_examples import add; print(add(2, 3))"
python -c "from cursor_cli_examples import Chain; print(Chain(10).add(5).multiply(2).subtract(3).value())"
python -c "from cursor_cli_examples import pipe; print(pipe(10, lambda x: x + 5, lambda x: x * 2, lambda x: x - 3))"
```
