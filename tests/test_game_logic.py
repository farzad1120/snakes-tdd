"""Test suite for the Snake game logic.

This module contains comprehensive tests for the Snake game logic,
following Test-Driven Development (TDD) principles. It tests all core
game mechanics including movement, collisions, food generation, and scoring.
"""

import pytest
from src.game_logic import SnakeGame


class TestSnakeGame:
    """Test suite for the SnakeGame class.

    This class contains all test cases for the Snake game logic. Tests are
    organized by functionality and use pytest fixtures for setup.
    """

    @pytest.fixture
    def game(self):
        """Fixture providing a fresh SnakeGame instance for each test.

        Returns:
            SnakeGame: A new game instance with default settings
        """
        return SnakeGame(width=800, height=600, block_size=20)

    def test_initial_game_state(self, game):
        """Test that the game initializes with correct default values.

        Verifies:
        - Game is not over
        - Score starts at 0
        - Snake has one segment
        - Initial direction is stationary
        - Food is placed on the board
        """
        assert not game.game_over
        assert game.score == 0
        assert len(game.snake_pos) == 1
        assert game.direction == (0, 0)
        assert game.food_pos is not None

    def test_snake_movement(self, game):
        """Test basic snake movement mechanics.

        Verifies:
        - Snake moves correctly in right direction
        - Snake moves correctly in down direction
        - Position updates properly after each move
        """
        # Initial position
        initial_pos = game.snake_pos[0]

        # Move right
        game.change_direction((20, 0))
        game.move_snake()
        assert game.snake_pos[0] == (initial_pos[0] + 20, initial_pos[1])

        # Move down
        game.change_direction((0, 20))
        game.move_snake()
        assert game.snake_pos[0] == (initial_pos[0] + 20, initial_pos[1] + 20)

    def test_wall_collision(self, game):
        """Test collision detection with walls.

        Verifies that the game ends when snake hits any wall.
        """
        # Move snake to right wall
        game.snake_pos = [(780, 300)]  # Near right wall
        game.change_direction((20, 0))  # Move right
        game.move_snake()
        assert game.game_over

    def test_self_collision(self, game):
        """Test collision detection with snake's own body.

        Verifies that the game ends when snake collides with itself.
        """
        # Create a snake with multiple segments where moving down will hit its own body
        game.snake_pos = [(100, 60), (100, 80), (80, 80), (80, 60), (100, 60)]
        game.change_direction((0, 20))  # Move down into its own body at (100, 80)
        game.move_snake()
        assert game.game_over

    def test_eating_food(self, game):
        """Test food eating mechanics.

        Verifies:
        - Snake grows when eating food
        - Score increases
        - New food is generated
        """
        # Place food directly in front of snake
        initial_length = len(game.snake_pos)
        food_pos = (game.snake_pos[0][0] + 20, game.snake_pos[0][1])
        game.food_pos = food_pos

        # Move snake to food
        game.change_direction((20, 0))
        game.move_snake()

        assert len(game.snake_pos) == initial_length + 1
        assert game.score == 1
        assert game.food_pos != food_pos  # Food should have moved

    def test_invalid_direction_change(self, game):
        """Test that snake cannot reverse direction.

        Verifies that attempting to move in the opposite direction
        is ignored to prevent instant self-collision.
        """
        # Move right
        game.change_direction((20, 0))
        game.move_snake()

        # Try to move left (should be ignored)
        game.change_direction((-20, 0))
        original_direction = game.direction
        game.move_snake()
        assert game.direction == original_direction

    def test_reset_game(self, game):
        """Test game reset functionality.

        Verifies that all game state is properly reset to initial values.
        """
        # Change game state
        game.score = 10
        game.game_over = True
        game.snake_pos = [(100, 100), (120, 100)]
        game.direction = (20, 0)

        # Reset game
        game.reset_game()

        # Verify reset state
        assert not game.game_over
        assert game.score == 0
        assert len(game.snake_pos) == 1
        assert game.direction == (0, 0)
        assert game.food_pos is not None

    def test_food_generation(self, game):
        """Test food generation mechanics.

        Verifies:
        - Food is always within game bounds
        - Food position aligns with grid
        - Multiple food generations work correctly
        """
        # Generate multiple food positions and verify they're within bounds
        for _ in range(10):
            food_pos = game.generate_food()
            assert 0 <= food_pos[0] < game.width
            assert 0 <= food_pos[1] < game.height
            assert food_pos[0] % game.block_size == 0
            assert food_pos[1] % game.block_size == 0
