class SnakeGame:
    def __init__(self, width=800, height=600, block_size=20):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.score = 0
        # Initialize snake in the middle of the screen
        self.snake_pos = [(self.width // 2, self.height // 2)]
        self.direction = (0, 0)
        self.food_pos = self.generate_food()

    def generate_food(self):
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
        return {
            "snake_positions": self.snake_pos,
            "food_position": self.food_pos,
            "score": self.score,
            "game_over": self.game_over,
        }
