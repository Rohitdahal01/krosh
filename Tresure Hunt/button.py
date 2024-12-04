import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Main Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load background image (replace with your own image)
background_image = pygame.image.load("assets\Background.png").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Load images for buttons (replace with your own images)
play_image = pygame.image.load("passets\startbutton.png").convert_alpha()
options_image = pygame.image.load("assets\optionsbutton.png").convert_alpha()
sound_image = pygame.image.load("assets\back.png").convert_alpha()
account_image = pygame.image.load("assets\back.png").convert_alpha()
exit_image = pygame.image.load("assets\exit.png").convert_alpha()

# Scale images if needed
button_width, button_height = 200, 50
play_image = pygame.transform.scale(play_image, (button_width, button_height))
options_image = pygame.transform.scale(options_image, (button_width, button_height))
sound_image = pygame.transform.scale(sound_image, (button_width, button_height))
account_image = pygame.transform.scale(account_image, (button_width, button_height))
exit_image = pygame.transform.scale(exit_image, (button_width, button_height))

# Button positions
play_button = pygame.Rect((WIDTH // 2 - 100, 150), (button_width, button_height))
options_button = pygame.Rect((WIDTH // 2 - 100, 220), (button_width, button_height))
sound_button = pygame.Rect((WIDTH // 2 - 100, 290), (button_width, button_height))
account_button = pygame.Rect((WIDTH // 2 - 100, 360), (button_width, button_height))
exit_button = pygame.Rect((WIDTH // 2 - 100, 430), (button_width, button_height))

def draw_main_menu():
    """Draw the main menu."""
    screen.blit(background_image, (0, 0))  # Draw the background image
    screen.blit(play_image, play_button.topleft)
    screen.blit(options_image, options_button.topleft)
    screen.blit(sound_image, sound_button.topleft)
    screen.blit(account_image, account_button.topleft)
    screen.blit(exit_image, exit_button.topleft)
    pygame.display.flip()

def play_page():
    """Simulates the Play page."""
    screen.fill(WHITE)
    pygame.display.set_caption("Play")
    pygame.display.flip()

def options_page():
    """Simulates the Options page."""
    screen.fill(WHITE)
    pygame.display.set_caption("Options")
    pygame.display.flip()

def sound_page():
    """Simulates the Sound page."""
    screen.fill(WHITE)
    pygame.display.set_caption("Sound")
    pygame.display.flip()

def account_page():
    """Simulates the Account page."""
    screen.fill(WHITE)
    pygame.display.set_caption("Account")
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    running = True
    current_page = "menu"  # Tracks which page the user is on

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                if current_page == "menu":
                    if play_button.collidepoint(mouse_pos):
                        current_page = "play"
                    elif options_button.collidepoint(mouse_pos):
                        current_page = "options"
                    elif sound_button.collidepoint(mouse_pos):
                        current_page = "sound"
                    elif account_button.collidepoint(mouse_pos):
                        current_page = "account"
                    elif exit_button.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if current_page != "menu":
                    current_page = "menu"

        if current_page == "menu":
            draw_main_menu()
        elif current_page == "play":
            play_page()
        elif current_page == "options":
            options_page()
        elif current_page == "sound":
            sound_page()
        elif current_page == "account":
            account_page()

        clock.tick(60)

if __name__ == "__main__":
    main()
