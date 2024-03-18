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
start_button_rect = start_button_img.get_rect(topright=(SCREEN_WIDTH - 20, 300))
quit_button_rect = quit_button_img.get_rect(topright=(SCREEN_WIDTH - 20, start_button_rect.bottom + 20))

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
                game_loop()

        if quit_button_rect.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def game_loop():
    global player_x, player_y, bg_x, current_frame, frame_count, player_img, is_moving
    
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    
    running = True
    while running:
        screen.fill((0, 0, 0))  # Fill the screen with the background color
        
        # Calculate the portion of the background to show based on player position
        bg_offset = player_x
        if bg_offset < 0:
            bg_offset = 0
        elif bg_offset > background_img.get_width() - SCREEN_WIDTH:
            bg_offset = background_img.get_width() - SCREEN_WIDTH

        screen.blit(background_img, (0, bg_y), (bg_offset, 0, SCREEN_WIDTH, SCREEN_HEIGHT))  # Draw visible portion of background
        
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            is_moving = True
        elif keys[pygame.K_RIGHT]:
            player_x += player_speed
            is_moving = True
        elif keys[pygame.K_UP]:
            player_y -= player_speed
            is_moving = True
        elif keys[pygame.K_DOWN]:
            player_y += player_speed
            is_moving = True
        else:
            is_moving = False

        # Keep player within screen bounds and limit movement to bottom third of the screen
        player_x = max(0, min(player_x, background_img.get_width() - SCREEN_WIDTH))

        # Update player animation
        if is_moving:
            frame_count += 1
            if frame_count >= 15:  # Adjust this value to control the animation speed
                frame_count = 0
                current_frame = (current_frame + 1) % len(player_animation_frames)
            player_img = player_animation_frames[current_frame]
        else:
            player_img = player_img_standing
        
        # Draw player
        player_rect = player_img.get_rect()
        player_rect.center = (player_x, player_y)
        screen.blit(player_img, player_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)  # Cap the frame rate at 60 frames per second

if __name__ == "__main__":
    main_menu()
