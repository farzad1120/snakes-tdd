"""Game logic module for the Snake game.

This module contains the core game logic for the Snake game, handling the snake's movement,
collision detection, food generation, and score tracking. It is designed to be independent
of any specific UI implementation.
"""

class SnakeGame:
    """Main game logic class for the Snake game.

    This class handles all the game mechanics including snake movement, collision detection,
    food generation, and score tracking. It maintains the game state and provides methods
    to manipulate and query that state.

    Attributes:
        width (int): Width of the game board in pixels
        height (int): Height of the game board in pixels
        block_size (int): Size of each snake segment and food block in pixels
        game_over (bool): Flag indicating if the game has ended
        score (int): Current game score
        snake_pos (list): List of (x, y) tuples representing snake segments
        direction (tuple): Current movement direction as (x, y)
        food_pos (tuple): Current food position as (x, y)
    """

    def __init__(self, width=800, height=600, block_size=20):
        """Initialize a new game instance.

        Args:
            width (int, optional): Width of game board. Defaults to 800.
            height (int, optional): Height of game board. Defaults to 600.
            block_size (int, optional): Size of game blocks. Defaults to 20.
        """
        self.width = width
        self.height = height
        self.block_size = block_size
        self.reset_game()

    def reset_game(self):
        """Reset the game to its initial state.

        This method resets all game variables to their starting values, including:
        - Placing the snake in the middle of the screen
        - Resetting the score to 0
        - Generating new food
        - Resetting game over state
        """
        self.game_over = False
        self.score = 0
        # Initialize snake in the middle of the screen
        self.snake_pos = [(self.width // 2, self.height // 2)]
        self.direction = (0, 0)
        self.food_pos = self.generate_food()

    def generate_food(self):
        """Generate new food at a random position.

        The food is placed at a random position on the game board, ensuring it doesn't
        appear on top of the snake. The position is aligned to the block size grid.

        Returns:
            tuple: (x, y) coordinates of the new food position
        """
        import random

        x = (
            round(random.randrange(0, self.width - self.block_size) / self.block_size)
            * self.block_size
        )
        y = (
            round(random.randrange(0, self.height - self.block_size) / self.block_size)
            * self.block_size
        )
        # Ensure food doesn't appear on snake
        while (x, y) in self.snake_pos:
            x = (
                round(
                    random.randrange(0, self.width - self.block_size) / self.block_size
                )
                * self.block_size
            )
            y = (
                round(
                    random.randrange(0, self.height - self.block_size) / self.block_size
                )
                * self.block_size
            )
        return (x, y)

    def change_direction(self, new_direction):
        """Change the snake's direction of movement.

        Prevents 180-degree turns by checking if the new direction is opposite
        to the current direction.

        Args:
            new_direction (tuple): New direction as (x, y) displacement
        """
        # Prevent 180-degree turns
        opposite_directions = {
            (self.block_size, 0): (-self.block_size, 0),
            (-self.block_size, 0): (self.block_size, 0),
            (0, self.block_size): (0, -self.block_size),
            (0, -self.block_size): (0, self.block_size),
        }
        if self.direction == (0, 0) or new_direction != opposite_directions.get(
            self.direction
        ):
            self.direction = new_direction

    def move_snake(self):
        """Move the snake in its current direction.

        Updates the snake's position based on its current direction. Handles:
        - Moving the snake's head
        - Checking for collisions with walls and self
        - Growing the snake when food is eaten
        - Updating the score
        - Generating new food when current food is eaten
        """
        if self.direction == (0, 0):
            return

        new_head = (
            self.snake_pos[0][0] + self.direction[0],
            self.snake_pos[0][1] + self.direction[1],
        )

        # Check for collisions with walls or self
        if (
            new_head[0] >= self.width
            or new_head[0] < 0
            or new_head[1] >= self.height
            or new_head[1] < 0
            or new_head in self.snake_pos[:-1]
        ):
            self.game_over = True
            return

        self.snake_pos.insert(0, new_head)

        # Check if snake ate food
        if new_head == self.food_pos:
            self.score += 1
            self.food_pos = self.generate_food()
        else:
            self.snake_pos.pop()

    def check_collision(self, position):
        """Check if a position collides with walls or snake body.

        Args:
            position (tuple): Position to check as (x, y)

        Returns:
            bool: True if collision detected, False otherwise
        """
        # Check wall collision
        if (
            position[0] >= self.width
            or position[0] < 0
            or position[1] >= self.height
            or position[1] < 0
        ):
            return True

        # Check self collision (excluding head)
        if position in self.snake_pos[:-1]:
            return True

        return False

    def get_state(self):
        """Get the current game state.

        Returns:
            dict: Current game state including:
                - snake_positions: List of all snake segment positions
                - food_position: Current food position
                - score: Current score
                - game_over: Whether the game has ended
        """
        return {
            "snake_positions": self.snake_pos,
            "food_position": self.food_pos,
            "score": self.score,
            "game_over": self.game_over,
        }
