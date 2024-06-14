import pygame
import random

# Initialize Pygame
pygame.init()

# Get screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set game window dimensions
GAME_WIDTH, GAME_HEIGHT = 300, 300

# Calculate the position to center the game window
x_pos = (SCREEN_WIDTH - GAME_WIDTH) // 2
y_pos = (SCREEN_HEIGHT - GAME_HEIGHT) // 2

# Set screen dimensions
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("TikTok Magic")

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Define animation parameters
animation_speed = 5
offset_x = 0
offset_y = 0

# Font setup
font = pygame.font.Font(None, 36)
text = font.render("Tap to see the magic!", True, WHITE)

# Main loop
running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black background

    # Draw fancy pattern with moving squares
    for i in range(0, GAME_WIDTH, 50):
        for j in range(0, GAME_HEIGHT, 50):
            color = random.choice(colors)
            pygame.draw.rect(screen, color, pygame.Rect(i + offset_x, j + offset_y, 50, 50))

    # Update animation parameters
    offset_x += animation_speed
    offset_y += animation_speed

    # Reset animation when it reaches the edge of the screen
    if offset_x >= 50:
        offset_x = 0
    if offset_y >= 50:
        offset_y = 0

    # Display text in the center
    text_rect = text.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))
    screen.blit(text, text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add event for engagement (e.g., increase views)
            print("View +1")  # You can replace this with your actual logic for increasing views

    pygame.display.flip()

    # Adjust frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
