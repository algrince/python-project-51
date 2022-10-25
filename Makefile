install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest -cov=page-loader --cov-report xml

lint: 
	poetry run flake8 page-loader

selfcheck:
	poetry check

check: selfcheck test lint
