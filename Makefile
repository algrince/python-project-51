install:
	poetry install

build:
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest -cov=page_loader --cov-report xml

lint: 
	poetry run flake8 page_loader

selfcheck:
	poetry check

check: selfcheck test lint
