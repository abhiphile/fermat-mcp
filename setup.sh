#!/bin/bash
set -e  # Exit on error

# Change to the directory where this script is located
cd "$(dirname "$0")"

VENV=".venv"

# Create virtual environment if not present
if [ ! -d "$VENV" ]; then
    echo "Creating virtual environment..."
    uv venv "$VENV"
    source "$VENV/bin/activate"
    uv pip install --upgrade pip
else
    echo "Virtual environment already exists"
fi

# Activate environment and install dependencies
echo "Installing dependencies..."
source "$VENV/bin/activate"

if [ ! -f "pyproject.toml" ]; then
    echo "ERROR: pyproject.toml not found"
    exit 1
fi

uv sync

# Start the MCP server
echo "Starting MCP server..."
python server.py