TEST_FLAGS = --cov
TEST_PATH = src/

.PHONY: install
install: poetry.lock
	poetry install $(POETRY_EXTRA)

.PHONY: format
format:
	isort -rc .
	black .

.PHONY: tests
tests:
	py.test $(TEST_FLAGS) $(TEST_PATH)

poetry.lock: pyproject.toml
	poetry lock

requirements.txt: poetry.lock
	poetry install $(POETRY_EXTRA)
	poetry show --no-dev | awk '{print $$1"=="$$2}' > $@
