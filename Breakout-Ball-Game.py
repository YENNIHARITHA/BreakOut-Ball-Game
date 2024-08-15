import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Paddle
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - paddle_height - 10
paddle_speed = 10

# Ball
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_dx = 5 * random.choice([-1, 1])
ball_dy = -5

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 20
bricks = []

for row in range(brick_rows):
    brick_row = []
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        brick_row.append(brick_rect)
    bricks.append(brick_row)

# Game loop
running = True
while running:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= screen_width - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y + ball_radius < paddle_y + paddle_height:
        ball_dy = -ball_dy

    # Ball collision with bricks
    for row in bricks:
        for brick in row:
            if brick.collidepoint(ball_x, ball_y):
                ball_dy = -ball_dy
                row.remove(brick)
                break

    # Draw paddle
    paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, paddle)

    # Draw ball
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Draw bricks
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, blue, brick)

    # Game over conditions
    if ball_y > screen_height:
        running = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
