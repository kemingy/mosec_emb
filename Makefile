PY_SOURCE=.

lint:
	@ruff check .

format:
	@ruff check --fix .
	@ruff format .

clean:
	@-rm -rf dist build __pycache__ *.egg-info __version__.py

build:
	@python -m build
