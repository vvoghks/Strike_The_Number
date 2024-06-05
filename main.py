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
font_size = 50
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
    button_width = 160
    button_height = 80
    button_rect = pygame.Rect(10, 10, button_width, button_height)
    pygame.draw.rect(window, pygame.Color('orange'), button_rect)
    restart_text = input_font.render("R", True, (0, 0, 0))
    text_rect = restart_text.get_rect(center=button_rect.center)
    window.blit(restart_text, text_rect)
    return button_rect

# Generate the random number once and print it to the shell
random_number = generate_random_number()
print(f"Random Number: {random_number}")

# Input variables
input_text = ''
disabled_digits = set()
input_values = []
max_values = 18
results = []
color_active = pygame.Color('lightskyblue3')
color = color_active

# Main loop
game_number = 1
running = True
game_won = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button clicked
                # Restart button clicked
                restart_button_rect = create_restart_button()
                if restart_button_rect.collidepoint(event.pos):
                    random_number = generate_random_number()
                    print(f"Random Number: {random_number}")
                    input_values.clear()
                    results.clear()
                    input_text = ''
                    disabled_digits.clear()
                    game_number += 1
                    game_won = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                # Restart the game
                random_number = generate_random_number()
                print(f"Random Number: {random_number}")
                input_values.clear()
                results.clear()
                input_text = ''
                disabled_digits.clear()
                game_number += 1
                game_won = False
            if not game_won and len(input_values) < max_values:
                if event.key == pygame.K_BACKSPACE:
                    if input_text:
                        disabled_digits.discard(input_text[-1])
                        input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(input_text) == 3:
                        balls, strikes = calculate_balls_and_strikes(random_number, input_text)
                        if strikes == 3:
                            result_text = "Strike Out"
                            game_won = True
                        else:
                            result_text = f"{balls}B - {strikes}S"
                        input_values.append(input_text)
                        results.append(result_text)
                        if len(input_values) > max_values:
                            input_values.pop(0)
                            results.pop(0)
                        input_text = ''
                        disabled_digits.clear()
                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    digit = event.key - pygame.K_0  # Convert key to digit value
                    if len(input_text) < 3 and str(digit) not in disabled_digits:
                        input_text += str(digit)
                        disabled_digits.add(str(digit))

    # Fill the screen with a white background
    window.fill((255, 255, 255))

    # Display "<Game #>" on the center top
    game_text = f"Game {game_number}"
    game_text_surface = font.render(game_text, True, (0, 0, 0))
    game_text_rect = game_text_surface.get_rect(center=(window_width // 2, 40))  # Adjust the y-coordinate as needed
    window.blit(game_text_surface, game_text_rect)

    # Render the input text
    input_display_text = font.render(input_text, True, (0, 0, 0))
    input_display_rect = input_display_text.get_rect(center=(window_width // 2, window_height // 2))

    # Draw the input text on the screen
    window.blit(input_display_text, input_display_rect)

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

    # Check if it's the 18th try or the game is won
    if len(input_values) == max_values or game_won:
        if game_won:
            # Display "YOU WIN!" on one line
            win_text = font.render("YOU WIN!", True, (0, 255, 0))
            win_rect = win_text.get_rect(center=(window_width // 2, window_height // 2 - 30))
            window.blit(win_text, win_rect)
        else:
            # Display "YOU LOSE!" on one line
            lose_text = font.render("YOU LOSE!", True, (255, 0, 0))
            lose_rect = lose_text.get_rect(center=(window_width // 2, window_height // 2 - 30))
            window.blit(lose_text, lose_rect)

            # Display "The answer is <number>." on the next line
            answer_text = font.render("The answer is " + random_number + ".", True, (255, 0, 0))
            answer_rect = answer_text.get_rect(center=(window_width // 2, window_height // 2 + 30))
            window.blit(answer_text, answer_rect)

        # Disable buttons and keyboard inputs
        input_text = ''  # Clear the input text
        disabled_digits = set()  # Clear disabled digits set

        # Display "Press 'r' to restart"
        restart_text = font.render("Press 'r' to restart", True, (0, 0, 255))
        restart_rect = restart_text.get_rect(center=(window_width // 2, window_height - 60))
        window.blit(restart_text, restart_rect)

    # Draw the restart button
    create_restart_button()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
