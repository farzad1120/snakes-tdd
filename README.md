# Snake Game

A classic Snake game implemented in Python using Pygame, following Test-Driven Development (TDD) principles.

## Project Structure

```
snakes/
├── src/
│   ├── snake_game.py    # Main game UI
│   └── game_logic.py    # Game logic
├── tests/
│   └── test_game_logic.py  # Unit tests
├── requirements.txt     # Project dependencies
├── pytest.ini          # Test configuration
├── Makefile           # Build and development commands
└── README.md           # This file
```

## Quick Start

The easiest way to get started is using the Makefile commands:

```bash
# Set up the project (creates virtual environment and installs dependencies)
make setup

# Run the game
make run
```

## Development Commands

The project includes a Makefile with various commands to help with development:

```bash
# Show all available commands
make help

# Install development dependencies
make install-dev

# Run tests
make test

# Run tests with coverage report
make coverage

# Run linting and formatting checks
make lint

# Format code using black
make format

# Clean up Python cache files and virtual environment
make clean
```

## Manual Setup

If you prefer not to use Make, you can set up the project manually:

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests with:
```bash
pytest
```

To see test coverage:
```bash
pytest --cov=src tests/
```

## Running the Game

To play the game:
```bash
python src/snake_game.py
```

## Game Controls

- Arrow keys to control snake direction
- Q to quit when game is over
- C to play again when game is over

## Development

This project follows Test-Driven Development (TDD) principles. When making changes:

1. Write a failing test first
2. Write the minimum code to make the test pass
3. Refactor if needed
4. Run the full test suite before committing changes

## Code Style

The project uses:
- `black` for code formatting
- `flake8` for code linting

Run style checks with:
```bash
make lint
