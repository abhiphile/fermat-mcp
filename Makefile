.PHONY: help setup venv install run test clean format lint check

# Variables
VENV = .venv
UV = uv
CONFIG = mcp_config.json

# Help message
help:
	@echo "Available commands:"
	@echo "  make setup       - Set up development environment"
	@echo "  make venv        - Create a virtual environment"
	@echo "  make install     - Install dependencies"
	@echo "  make run         - Run the MCP server"
	@echo "  make test        - Run tests"
	@echo "  make format      - Format code with Black and Ruff"
	@echo "  make lint        - Lint code with Ruff"
	@echo "  make check       - Run all checks (lint, format, test)"
	@echo "  make clean       - Clean up temporary files"

# Setup development environment
setup: venv install

# Create virtual environment
venv:
	@echo "Creating virtual environment with uv..."
	@if [ ! -d "$(VENV)" ]; then \
		$(UV) venv $(VENV); \
		. $(VENV)/bin/activate && $(UV) pip install --upgrade pip; \
	fi

# Install dependencies
install: venv
	@echo "Installing dependencies..."
	@. $(VENV)/bin/activate && \
	$(UV) pip install -e . && \
	$(UV) pip install -e ".[dev]"

# Run the MCP server
run: venv
	@if [ ! -f "$(CONFIG)" ]; then \
		echo "Creating default MCP configuration file..."; \
		echo '{"transport": "stdio", "log_level": "info"}' > $(CONFIG); \
		echo "Created $(CONFIG) with default settings"; \
	fi
	@echo "Starting MCP server..."
	@. $(VENV)/bin/activate && \
	$(UV) run server.py

# Run tests
test: venv
	@echo "Running tests..."
	@. $(VENV)/bin/activate && \
	$(UV) run pytest -v

# Format code
format: venv
	@echo "Formatting code..."
	@. $(VENV)/bin/activate && \
	$(UV) run ruff format . && \
	$(UV) run black .

# Lint code
lint: venv
	@echo "Linting code..."
	@. $(VENV)/bin/activate && \
	$(UV) run ruff check .

# Run all checks
check: lint format test

# Clean up
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -f .coverage
	rm -f .mypy_cache

# Show help by default
.DEFAULT_GOAL := help
