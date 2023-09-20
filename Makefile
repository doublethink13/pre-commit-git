SHELL := /bin/bash

usage:
	@echo "Usage"
	@echo "	usage (default)"
	@echo "	usage setup_python_interpreter"
	@echo "	usage setup_venv"
	@echo "	usage install_requirements"
	@echo "	usage apply_formatting"
	@echo "	usage lint"
	@echo "	usage test_one TEST='name_of_test'"
	@echo "	usage test_all"
	@echo "	usage coverage"

setup_python_interpreter:
	@pyenv install --skip-existing 3.11.2
	@pyenv local 3.11.2

setup_venv:
	@python -m venv venv

install_requirements:
	@pip install -r requirements.txt

apply_formatting:
	@black .
	@isort .

lint:
	@python -m black . --check
	@python -m isort . --check-only
	@python -m flake8 .
	@python -m mypy .

test_one:
	@pytest -vv -s -k $(TEST)

test_all:
	@pytest tests

coverage:
	@python -m coverage run --source app -m pytest tests
	@python -m coverage report