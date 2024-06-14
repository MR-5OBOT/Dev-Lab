# my first python game test for my tiktok content
# created at 12-06-2024

# my first python game test for my tiktok content
# created at 12-06-2024

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 700, 700  # Switched width and height for 9:16 aspect ratio
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Catcher")

# Background music
pygame.mixer.music.load('bg_music.wav')  # Replace 'bg_music.wav' with your file
pygame.mixer.music.play(-1)  # Play music infinitely

# Load images
basket_img = pygame.image.load('./images/basket.jpg').convert_alpha()  # Replace 'basket.jpg' with your file
fruit_img = pygame.image.load('./images/fruit.jpg').convert_alpha()  # Replace 'fruit.jpg' with your file

# Fonts
font = pygame.font.Font(None, 36)

# Basket
basket_width = 100  # Adjusted for TikTok layout
basket_height = 100  # Adjusted for TikTok layout
basket_x = (WIDTH - basket_width) // 2
basket_y = HEIGHT - 2 * basket_height
basket_speed = 10

# Fruits
fruits = []
fruit_speed = 5  # Adjusted for TikTok layout
fruit_size = 50
spawn_delay = 60
spawn_timer = spawn_delay

# Score
score = 0

# Game over flag
game_over = False

# Game over text
game_over_text = font.render("Game Over", True, (255, 255, 255))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Set background color to black

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    if not game_over:
        # Move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        # Keep basket within screen bounds
        basket_x = max(0, min(basket_x, WIDTH - basket_width))

        # Spawn fruits
        spawn_timer -= 1
        if spawn_timer <= 0:
            fruits.append([random.randint(0, WIDTH - fruit_size), -fruit_size])
            spawn_timer = spawn_delay

        # Move and draw fruits
        for fruit_pos in fruits:
            fruit_pos[1] += fruit_speed
            screen.blit(fruit_img, fruit_pos)

        # Draw basket
        screen.blit(basket_img, (basket_x, basket_y))

        # Collision detection
        for fruit_pos in fruits[:]:
            if pygame.Rect(fruit_pos[0], fruit_pos[1], fruit_size, fruit_size).colliderect(
                    pygame.Rect(basket_x, basket_y, basket_width, basket_height)):
                fruits.remove(fruit_pos)
                score += 1
                # Add particle effects
                # Add sound effect when catching a fruit

        # Display score
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()
        clock.tick(60)
    else:
        # Display game over screen
        screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, (HEIGHT - game_over_text.get_height()) // 2))
        pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
