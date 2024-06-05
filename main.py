import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
window_width = 1440
window_height = 810
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

# Button settings
button_width = 100
button_height = 60
button_margin = 10

# Create buttons for digits, backspace, and enter
buttons = []
button_labels = [
    '1', '2', '3', '4', '5', 'Backspace',
    '6', '7', '8', '9', '0', 'Enter'
]

for i, label in enumerate(button_labels):
    x = (i % 6) * (button_width + button_margin) + button_margin
    y = window_height - (2 - i // 6) * (button_height + button_margin) - button_margin
    rect = pygame.Rect(x, y, button_width, button_height)
    buttons.append((rect, label))

# Input variables
input_text = ''
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
            for rect, label in buttons:
                if rect.collidepoint(event.pos):
                    if label == 'Backspace':
                        input_text = input_text[:-1]
                    elif label == 'Enter':
                        input_text = ''
                    else:
                        if len(input_text) < 3:
                            input_text += label

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

    # Draw buttons
    for rect, label in buttons:
        pygame.draw.rect(window, color_inactive, rect)
        text_surface = input_font.render(label, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        window.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
