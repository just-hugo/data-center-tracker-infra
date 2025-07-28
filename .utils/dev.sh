#!/bin/zsh  

# Virtual environment management
alias dev=". .venv/bin/activate"

alias off="deactivate"

# Linting and formatting
alias lint="ruff check"

alias format="ruff format"

alias fix="ruff check --fix"

# Testing
alias test="pytest"