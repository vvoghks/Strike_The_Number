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
input_font = pygame.font.Font(None, 50)

# Function to generate a random three-digit number with no repeating digits
def generate_random_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:3])

# Generate the random number once
random_number = generate_random_number()

# Input variables
input_box = pygame.Rect(20, window_height - 60, window_width - 40, 40)
input_text = ''
input_active = False
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box, toggle the active variable.
            if input_box.collidepoint(event.pos):
                input_active = not input_active
            else:
                input_active = False
            # Change the current color of the input box.
            color = color_active if input_active else color_inactive
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    # Optionally process the input text here
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

    # Fill the screen with a white background
    window.fill((255, 255, 255))

    # Render the random three-digit number
    random_number_text = font.render(random_number, True, (0, 0, 0))
    random_number_rect = random_number_text.get_rect(center=(window_width // 2 - 100, window_height // 2))

    # Render the input text next to the random number
    input_display_text = font.render(input_text, True, (0, 0, 0))
    input_display_rect = input_display_text.get_rect(midleft=(random_number_rect.right + 20, window_height // 2))

    # Draw the random number and input text on the screen
    window.blit(random_number_text, random_number_rect)
    window.blit(input_display_text, input_display_rect)

    # Render the input text in the input box
    input_surface = input_font.render(input_text, True, (0, 0, 0))
    window.blit(input_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(window, color, input_box, 2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
