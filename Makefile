.PHONY: models.load test lint clean release tag

PROJECT_NAME=fraud_checker

test:
	@echo "run tests"
	@pytest

lint:
	@mypy --ignore-missing-imports $(PROJECT_NAME)
	@flake8 $(PROJECT_NAME)
	@flake8 --append-config=flake8.tests.ini tests

clean:
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -rf htmlcov
	@rm -rf .coverage
	@rm -rf .coverage.xml
	@rm -rf build/

bump:= patch

release:
	@VERSION=$$(poetry version ${bump}); git add pyproject.toml; echo "$${VERSION}"; git commit -m "$${VERSION}"
	@VERSION=$$(poetry run python -c "$$get_version"); echo "set tag: $${VERSION}"; git tag "$${VERSION}"
