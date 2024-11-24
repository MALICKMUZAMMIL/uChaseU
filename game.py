import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase and Collect Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game clock
clock = pygame.time.Clock()
FPS = 60

# Load Images
player1_img = pygame.image.load("player.png")  # Replace with your image file
player1_img = pygame.transform.scale(player1_img, (50, 50))  # Scale to 50x50

player2_img = pygame.image.load("player.png")  # Replace with your image file
player2_img = pygame.transform.scale(player2_img, (50, 50))  # Scale to 50x50

food_img = pygame.image.load("food.png")  # Replace with your image file
food_img = pygame.transform.scale(food_img, (30, 30))  # Scale to 30x30

# Player positions
player1 = pygame.Rect(WIDTH // 4, HEIGHT // 2, 50, 50)  # Initial position
player_speed = 5

player2 = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)  # Initial position
chaser_speed = 2

# Food
food = pygame.Rect(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 30, 30)

# Score
score = 0

# Game Over flag
game_over = False

# Font
font = pygame.font.Font(None, 36)

# Game Loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Movement for Player 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player1.top > 0:
            player1.y -= player_speed
        if keys[pygame.K_DOWN] and player1.bottom < HEIGHT:
            player1.y += player_speed
        if keys[pygame.K_LEFT] and player1.left > 0:
            player1.x -= player_speed
        if keys[pygame.K_RIGHT] and player1.right < WIDTH:
            player1.x += player_speed

        # Movement for Player 2 (Chaser)
        if player2.x < player1.x:
            player2.x += chaser_speed
        if player2.x > player1.x:
            player2.x -= chaser_speed
        if player2.y < player1.y:
            player2.y += chaser_speed
        if player2.y > player1.y:
            player2.y -= chaser_speed

        # Check collision with food
        if player1.colliderect(food):
            score += 1
            food.x = random.randint(0, WIDTH - 30)
            food.y = random.randint(0, HEIGHT - 30)

        # Check collision with Chaser
        if player1.colliderect(player2):
            game_over = True

    # Drawing everything
    screen.fill(WHITE)
    screen.blit(player1_img, (player1.x, player1.y))  # Draw Player 1
    screen.blit(player2_img, (player2.x, player2.y))  # Draw Player 2
    screen.blit(food_img, (food.x, food.y))  # Draw Food

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Game Over screen
    if game_over:
        game_over_text = font.render("Game Over! Press R to Restart", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Restart the game
            player1 = pygame.Rect(WIDTH // 4, HEIGHT // 2, 50, 50)
            player2 = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
            food = pygame.Rect(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 30, 30)
            score = 0
            game_over = False

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
