#####################################################################
# Make file configs
#####################################################################
.PHONY: clean clean-test clean-pyc help requirements upgrade venv
.DEFAULT_GOAL := help
VENV = .env


######################################################################
# Management and Utility targets
######################################################################

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@grep '^[a-zA-Z]' $(MAKEFILE_LIST) | sort | awk -F ':.*?## ' 'NF==2 {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

clean: clean-pyc clean-test clean-docs-build ## Remove all build, test, coverage and Python artifacts

clean-pyc: ## Remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## Remove test and coverage artifacts
	rm -fr .mypy_cache/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr *.egg-info/

clean-docs-build: ## Remove docs and build artifacts
	rm -fr build/
	rm -fr dist/
	rm -rf docs/build/

docs-requirements: ## Install docs requirements
	pip3 install -qr requirements/docs.txt

requirements: ## Install development requirements
	pip3 install -r requirements/dev.txt

build: docs-requirements ## Build the project
	export DJANGO_SETTINGS_MODULE=test_settings.py
	python setup.py bdist_wheel
	cd docs && $(MAKE) html

venv: ## Create a virtual env and install test and production requirements
	python3.5 -m venv $(VENV)
	source $(VENV)/bin/activate
	pip3 install --upgrade pip

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: ## Upgrade requirement pins.
	pip3 install -qr requirements/pip-tools.txt
	pip-compile requirements/base.in --rebuild --upgrade -o requirements/base.txt
	pip-compile requirements/test.in --rebuild --upgrade -o requirements/test.txt
	pip-compile requirements/quality.in --rebuild --upgrade -o requirements/quality.txt
	pip-compile requirements/docs.in --rebuild --upgrade -o requirements/docs.txt
	pip-compile requirements/compatibility.in --rebuild --upgrade -o requirements/compatibility.txt
	pip-compile requirements/dev.in --rebuild --upgrade -o requirements/dev.txt
	pip-compile requirements/pip-tools.in --rebuild --upgrade -o requirements/pip-tools.txt
	# Delete django pin from test.txt so that tox can control Django version.
	sed '/^[dD]jango==/d' requirements/test.txt > requirements/test.tmp
	mv requirements/test.tmp requirements/test.txt


######################################################################
# Management and Utility targets
######################################################################

test: test-python test-quality ## Run all tests.

test-quality: ## Uses pep8 to check the quality of Code
	pycodestyle --show-source
	isort --recursive --check-only django_view_permissions setup.py
	pylint -j 0 django_view_permissions

test-python: ## Run python tests
	python -Wd -m pytest

test-docs: build ## Run docs tests
	twine check dist/*
