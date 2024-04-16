
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width = 500
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Define the snake class
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "right"
        self.size = 10
        self.body = []

    def move(self):
        if self.direction == "right":
            self.x += self.size
        elif self.direction == "left":
            self.x -= self.size
        elif self.direction == "up":
            self.y -= self.size
        elif self.direction == "down":
            self.y += self.size

        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def change_direction(self, direction):
        self.direction = direction

    def grow(self):
        self.body.append((self.x, self.y))

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(display, green, [x, y, self.size, self.size])

# Define the food class
class Food:
    def __init__(self):
        self.x = random.randrange(0, width - 10, 10)
        self.y = random.randrange(0, height - 10, 10)
        self.size = 10

    def draw(self):
        pygame.draw.rect(display, red, [self.x, self.y, self.size, self.size])

# Initialize the snake and food
snake = Snake(250, 250)
food = Food()

# Set up the game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction("right")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("left")
            elif event.key == pygame.K_UP:
                snake.change_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("down")

    # Move the snake
    snake.move()

    # Check for collision with the food
    if snake.x == food.x and snake.y == food.y:
        snake.grow()
        food = Food()

    # Check for collision with the walls
    if snake.x < 0 or snake.x >= width or snake.y < 0 or snake.y >= height:
        game_over = True

    # Check for collision with the body
    for x, y in snake.body[1:]:
        if snake.x == x and snake.y == y:
            game_over = True

    # Draw the screen
    display.fill(white)
    snake.draw()
    food.draw()
    pygame.display.update()

    # Set the frame rate
    clock.tick(10)

# Quit Pygame
