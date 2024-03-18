import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Luuranki of The Times")

# Get the directory of the script
current_dir = os.path.dirname(__file__)
image_folder = os.path.join(current_dir, "images")

# Load title image
title_img = pygame.image.load(os.path.join(image_folder, "title.png")).convert_alpha()
title_img = pygame.transform.scale(title_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load button images
start_button_img = pygame.image.load(os.path.join(image_folder, "start.png")).convert_alpha()
quit_button_img = pygame.image.load(os.path.join(image_folder, "quit.png")).convert_alpha()

# Calculate button positions
button_width = start_button_img.get_width()
button_height = start_button_img.get_height()
start_button_rect = start_button_img.get_rect(topleft=(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2))
quit_button_rect = quit_button_img.get_rect(topleft=(SCREEN_WIDTH // 3, start_button_rect.bottom + 20))

def main_menu():
    running = True
    while running:
        screen.blit(title_img, (0, 0))  # Draw title image

        mx, my = pygame.mouse.get_pos()

        screen.blit(start_button_img, start_button_rect)
        screen.blit(quit_button_img, quit_button_rect)

        if start_button_rect.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                # Start the game
                import game
                game.game_loop()

        if quit_button_rect.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
