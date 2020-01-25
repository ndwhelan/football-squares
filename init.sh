#!/usr/bin/env bash

set -u

PYTHON_VERSION="3.7.2"
VIRTUAL_ENV_NAME="football-squares"

# Create the virtual environment and set it as the one to use
# If you don't include "system" then external commands like `hobo' may fail
echo "Creating pyenv virtual environment and installing packages..."
pyenv install --skip-existing "${PYTHON_VERSION}"
pyenv virtualenv "${PYTHON_VERSION}" "${VIRTUAL_ENV_NAME}"
pyenv local "${VIRTUAL_ENV_NAME}"

# Install development requirements so we can setup pre-commit hooks
echo "Installing requirements..."
python -m pip install -r requirements.text
pyenv rehash  # this will make sure the package scripts are in the path

# Install git hooks to help our workflow
echo "Setting up Git hooks..."
pre-commit install

echo "Done!"
