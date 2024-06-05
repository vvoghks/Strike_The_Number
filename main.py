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
table_font = pygame.font.Font(None, 36)

# Function to generate a random three-digit number with no repeating digits
def generate_random_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return ''.join(digits[:3])

# Function to calculate balls and strikes
def calculate_balls_and_strikes(random_num, input_num):
    strikes = sum(1 for i in range(3) if random_num[i] == input_num[i])
    balls = sum(1 for i in range(3) if input_num[i] in random_num and random_num[i] != input_num[i])
    return balls, strikes

# Function to create a rectangular restart button
def create_restart_button():
    button_width = 100
    button_height = 40
    button_rect = pygame.Rect(10, 10, button_width, button_height)
    pygame.draw.rect(window, pygame.Color('orange'), button_rect)
    restart_text = input_font.render("RE", True, (0, 0, 0))
    text_rect = restart_text.get_rect(center=button_rect.center)
    window.blit(restart_text, text_rect)
    return button_rect

# Generate the random number once and print it to the shell
random_number = generate_random_number()
print(f"Random Number: {random_number}")

# Button settings
button_width = 100
button_height = 60
button_margin = 10

# Create buttons for digits, backspace, and enter
buttons = []
button_labels = [
    '1', '2', '3', '4', '5', '<<',
    '6', '7', '8', '9', '0', '>>'
]

for i, label in enumerate(button_labels):
    x = (i % 6) * (button_width + button_margin) + button_margin
    y = window_height - (2 - i // 6) * (button_height + button_margin) - button_margin
    rect = pygame.Rect(x, y, button_width, button_height)
    buttons.append((rect, label))

# Input variables
input_text = ''
disabled_digits = set()
input_values = []
max_values = 18
results = []
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
            if event.button == 1:  # Left mouse button clicked
                for rect, label in buttons:
                    if rect.collidepoint(event.pos):
                        if label == '<<':
                            if input_text:
                                disabled_digits.discard(input_text[-1])
                                input_text = input_text[:-1]
                        elif label == '>>':
                            if len(input_text) == 3:
                                balls, strikes = calculate_balls_and_strikes(random_number, input_text)
                                if strikes == 3:
                                    result_text = "Strike Out"
                                else:
                                    result_text = f"{balls}B - {strikes}S"
                                input_values.append(input_text)
                                results.append(result_text)
                                if len(input_values) > max_values:
                                    input_values.pop(0)
                                    results.pop(0)
                                input_text = ''
                                disabled_digits.clear()
                        else:
                            if len(input_text) < 3 and label not in disabled_digits:
                                input_text += label
                                disabled_digits.add(label)
                # Restart button clicked
                restart_button_rect = create_restart_button()
                if restart_button_rect.collidepoint(event.pos):
                    random_number = generate_random_number()
                    print(f"Random Number: {random_number}")
                    input_values.clear()
                    results.clear()
                    input_text = ''
                    disabled_digits.clear()

    # Fill the screen with a white background
    window.fill((255, 255, 255))

    # Render the input text
    input_display_text = font.render(input_text, True, (0, 0, 0))
    input_display_rect = input_display_text.get_rect(center=(window_width // 2, window_height // 2))

    # Draw the input text on the screen
    window.blit(input_display_text, input_display_rect)

    # Draw buttons
    for rect, label in buttons:
        button_color = color_inactive
        if label == '>>' and len(input_text) != 3:
            button_color = pygame.Color('grey')
        pygame.draw.rect(window, button_color, rect)
        text_color = (0, 0, 0) if label not in disabled_digits or label in ['<<', '>>'] else (128, 128, 128)
        text_surface = input_font.render(label, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        window.blit(text_surface, text_rect)

    # Draw 2-by-18 table
    table_x = window_width - 300
    table_y = 50
    cell_width = 140
    cell_height = 40
    for row in range(18):
        for col in range(2):
            cell_rect = pygame.Rect(table_x + col * cell_width, table_y + row * cell_height, cell_width, cell_height)
            pygame.draw.rect(window, pygame.Color('black'), cell_rect, 1)
            if col == 0 and row < len(input_values):
                value_text = table_font.render(input_values[row], True, (0, 0, 0))
                value_rect = value_text.get_rect(center=cell_rect.center)
                window.blit(value_text, value_rect)
            if col == 1 and row < len(results):
                result_text = table_font.render(results[row], True, (0, 0, 0))
                result_rect = result_text.get_rect(center=cell_rect.center)
                window.blit(result_text, result_rect)

    # Draw the restart button
    create_restart_button()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
