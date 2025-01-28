"""Snake Game UI Module

This module implements the graphical user interface for the Snake game using Pygame.
It handles all the display logic, user input, and game loop while delegating game
mechanics to the game_logic module.
"""

import pygame
import sys
from game_logic import SnakeGame

# Initialize pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)


class SnakeGameUI:
    """Pygame-based user interface for the Snake game.

    This class handles all the graphical aspects of the game including:
    - Rendering the game state
    - Handling user input
    - Managing the game loop
    - Displaying score and messages

    Attributes:
        screen (pygame.Surface): The main game display surface
        clock (pygame.time.Clock): Game clock for controlling frame rate
        font_style (pygame.font.Font): Font for general messages
        score_font (pygame.font.Font): Font for score display
        game (SnakeGame): The game logic instance
    """

    def __init__(self):
        """Initialize the game UI.

        Sets up the Pygame window, loads fonts, and initializes the game logic.
        """
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.game = SnakeGame(WIDTH, HEIGHT, BLOCK_SIZE)

    def display_score(self):
        """Display the current score on the screen.

        Renders the score in the top-left corner using the score font.
        """
        value = self.score_font.render(f"Your Score: {self.game.score}", True, GREEN)
        self.screen.blit(value, [0, 0])

    def display_message(self, msg, color):
        """Display a message on the screen.

        Args:
            msg (str): Message to display
            color (tuple): RGB color tuple for the message
        """
        mesg = self.font_style.render(msg, True, color)
        self.screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

    def draw_snake(self):
        """Draw the snake on the screen.

        Renders each segment of the snake as a black rectangle.
        """
        for pos in self.game.snake_pos:
            pygame.draw.rect(
                self.screen, BLACK, [pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE]
            )

    def draw_food(self):
        """Draw the food on the screen.

        Renders the food as a green rectangle.
        """
        pygame.draw.rect(
            self.screen,
            GREEN,
            [self.game.food_pos[0], self.game.food_pos[1], BLOCK_SIZE, BLOCK_SIZE],
        )

    def handle_input(self):
        """Handle user input events.

        Processes keyboard events for game control and window closing.
        Arrow keys control snake direction.

        Returns:
            bool: False if the game should exit, True otherwise
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.change_direction((-BLOCK_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    self.game.change_direction((BLOCK_SIZE, 0))
                elif event.key == pygame.K_UP:
                    self.game.change_direction((0, -BLOCK_SIZE))
                elif event.key == pygame.K_DOWN:
                    self.game.change_direction((0, BLOCK_SIZE))
        return True

    def game_loop(self):
        """Main game loop.

        Handles the core game flow including:
        - Processing user input
        - Updating game state
        - Rendering graphics
        - Managing game over state
        """
        running = True
        while running:
            if self.game.game_over:
                self.screen.fill(BLUE)
                self.display_message("You Lost! Press Q-Quit or C-Play Again", RED)
                self.display_score()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            return
                        if event.key == pygame.K_c:
                            self.game.reset_game()
                            break
                    if event.type == pygame.QUIT:
                        return
            else:
                running = self.handle_input()
                self.game.move_snake()

                self.screen.fill(WHITE)
                self.draw_food()
                self.draw_snake()
                self.display_score()

                pygame.display.update()
                self.clock.tick(SNAKE_SPEED)


def main():
    """Entry point for the game.

    Creates and runs the game instance, handling cleanup on exit.
    """
    game = SnakeGameUI()
    game.game_loop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
