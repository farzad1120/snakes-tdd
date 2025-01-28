.PHONY: help setup clean test coverage lint run install-dev

# Default target when just running 'make'
help:
	@echo "Available commands:"
	@echo "  make setup      - Create virtual environment and install dependencies"
	@echo "  make clean      - Remove Python cache files and virtual environment"
	@echo "  make test       - Run tests"
	@echo "  make coverage   - Run tests with coverage report"
	@echo "  make lint       - Run code linting (flake8) and formatting (black)"
	@echo "  make run        - Run the Snake game"
	@echo "  make install-dev- Install development dependencies"

# Create virtual environment and install dependencies
setup:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Install development dependencies
install-dev:
	pip install flake8 black pytest-cov

# Clean Python cache files and virtual environment
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	rm -rf venv/

# Run tests
test:
	python -m pytest

# Run tests with coverage report
coverage:
	python -m pytest --cov=src tests/ --cov-report=html
	@echo "Coverage report generated in htmlcov/index.html"

# Run linting and formatting
lint:
	flake8 src tests
	black src tests --check

# Format code
format:
	black src tests

# Run the game
run:
	python src/snake_game.py
