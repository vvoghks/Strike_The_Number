import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
window_width = 960
window_height = 540
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Strike The Number")

# Set up the font
font_size = 100
font = pygame.font.Font(None, font_size)

# Function to generate a random three-digit number
def generate_random_number():
    return random.randint(100, 999)

# Generate the random number once
random_number = generate_random_number()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a white background
    window.fill((255, 255, 255))

    # Render the random three-digit number
    text = font.render(str(random_number), True, (0, 0, 0))

    # Get the text rect and center it on the screen
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2))

    # Draw the text on the screen
    window.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
