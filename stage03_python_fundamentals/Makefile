.PHONY: help install dev run-nb lint fmt precommit

help:
	@echo "make install     # pip install -e ."
	@echo "make dev         # install dev tools (pre-commit, black, isort, flake8)"
	@echo "make precommit   # install pre-commit hooks"
	@echo "make fmt         # format with black & isort"
	@echo "make lint        # run flake8"

install:
	pip install -e .

dev:
	pip install pre-commit black isort flake8

precommit: dev
	pre-commit install

fmt:
	black src notebooks
	isort src notebooks

lint:
	flake8 src