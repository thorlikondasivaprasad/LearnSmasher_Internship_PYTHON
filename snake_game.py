import pygame
import random

# Game settings
WIDTH = 800
HEIGHT = 600
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake segment size
SEGMENT_SIZE = 20

# Initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.segments = [(WIDTH / 2, HEIGHT / 2)]
        self.dx = SEGMENT_SIZE
        self.dy = 0
        self.score = 0

    def move(self):
        x, y = self.segments[0]
        x += self.dx
        y += self.dy
        if x >= WIDTH:
            x = 0
        elif x < 0:
            x = WIDTH - SEGMENT_SIZE
        if y >= HEIGHT:
            y = 0
        elif y < 0:
            y = HEIGHT - SEGMENT_SIZE

        self.segments.insert(0, (x, y))
        if self.segments[0] == food.position:
            self.score += 1
            food.spawn()
        else:
            self.segments.pop()

        for segment in self.segments[1:]:
            if self.segments[0] == segment:
                self.game_over()

    def game_over(self):
        pygame.quit()
        quit()

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SEGMENT_SIZE, SEGMENT_SIZE))

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        x = random.randint(0, WIDTH - SEGMENT_SIZE)
        y = random.randint(0, HEIGHT - SEGMENT_SIZE)
        self.position = (x // SEGMENT_SIZE * SEGMENT_SIZE, y // SEGMENT_SIZE * SEGMENT_SIZE)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], SEGMENT_SIZE, SEGMENT_SIZE))

snake = Snake()
food = Food()

running = True
while running:
    # Game loop
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy != SEGMENT_SIZE:
                snake.dx = 0
                snake.dy = -SEGMENT_SIZE
            elif event.key == pygame.K_DOWN and snake.dy != -SEGMENT_SIZE:
                snake.dx = 0
                snake.dy = SEGMENT_SIZE
            elif event.key == pygame.K_LEFT and snake.dx != SEGMENT_SIZE:
                snake.dx = -SEGMENT_SIZE
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx != -SEGMENT_SIZE:
                snake.dx = SEGMENT_SIZE
                snake.dy = 0

    snake.move()

    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()

pygame.quit()
