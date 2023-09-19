SHELL := /bin/bash

usage:
	@echo "Usage"
	@echo "	usage (default)"
	@echo "	usage setup_python_interpreter"
	@echo "	usage setup_venv"
	@echo "	usage install_requirements"
	@echo "	usage apply_formatting"
	@echo "	usage lint"

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
