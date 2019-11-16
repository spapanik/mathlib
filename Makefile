PYTEST_FLAGS = -ra
PYTEST_PATH = tests/

poetry.lock: pyproject.toml
	poetry lock

requirements.txt: poetry.lock
	poetry install $(POETRY_EXTRA)
	poetry show | awk '{print $$1"=="$$2}' > $@

.PHONY: format
format:
	black .
	isort -rc .

.PHONY: tests
tests:
	pytest $(PYTEST_FLAGS) $(PYTEST_PATH)
