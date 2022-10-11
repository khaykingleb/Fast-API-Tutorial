SHELL := /bin/bash
VERSION := 0.1.0

##==================================================================================================
##@ Helper

help: ## Display help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage: \033[36m\033[0m\n"} /^[a-zA-Z\.\%-]+:.*?##/ { printf "  \033[36m%-24s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help

##==================================================================================================
##@ Repo initialization

repo-pre-commit: ## Install pre-commit
	pre-commit install
	pre-commit install -t commit-msg
.PHONY: repo-pre-commit

repo-deps: ## Install dependencies
	poetry install
.PHONY: repo-deps

repo-env: ## Configure environment variables
	cat .test.env  > .env
	echo "dotenv" > .envrc
.PHONY: repo-env

repo-init: repo-pre-commit repo-deps repo-env ## Initialize repository by executing above commands
.PHONY: repo-init

##==================================================================================================
##@ Secrets

create-detect-secrets-baseline:  ## Create or update .secrets.baseline file
	poetry run detect-secrets scan > .secrets.baseline
.PHONY: create-detect-secrets-baseline

##==================================================================================================
##@ Checks

mypy: ## Run type checker
	poetry run mypy
.PHONY:	mypy

##==================================================================================================
##@ Cleaning

clean-general: ## Delete general files
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".trash" | xargs rm -rf
	rm -f .coverage
.PHONY: clean-general

clean-all: clean-general ## Delete all "junk" files
.PHONY: clean-all

##==================================================================================================
##@ Miscellaneous

update-pre-commit-hooks:
	pre-commit autoupdate
.PHONY: update-pre-commit-hooks
