install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff --fix

format:
	uv run ruff format

test-coverage:
	uv run pytest --cov=python-project-50 --cov-report xml