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

# Load background image
background_img = pygame.image.load(os.path.join(image_folder, "street_background_wide.png")).convert_alpha()
background_height = SCREEN_HEIGHT  # Set background height to match screen height

# Load player images and scale down
player_standing_img = pygame.image.load(os.path.join(image_folder, "player_standing.png")).convert_alpha()
player_moving1_img = pygame.image.load(os.path.join(image_folder, "player_moving1.png")).convert_alpha()
player_moving2_img = pygame.image.load(os.path.join(image_folder, "player_moving2.png")).convert_alpha()

player_scale = 0.5  # Scale factor for player
player_standing_img = pygame.transform.scale(player_standing_img, (int(player_standing_img.get_width() * player_scale), int(player_standing_img.get_height() * player_scale)))
player_moving1_img = pygame.transform.scale(player_moving1_img, (int(player_moving1_img.get_width() * player_scale), int(player_moving1_img.get_height() * player_scale)))
player_moving2_img = pygame.transform.scale(player_moving2_img, (int(player_moving2_img.get_width() * player_scale), int(player_moving2_img.get_height() * player_scale)))

# Set player animation variables
player_images = [player_standing_img, player_moving1_img, player_moving2_img]
current_player_image = 0
animation_tick = 0
animation_speed = 1  # Adjust for animation speed

# Initialize player variables
player_width, player_height = player_standing_img.get_size()
player_x = SCREEN_WIDTH // 3  # Start at the center of the screen horizontally
player_y = SCREEN_HEIGHT * 3 // 4  # Start at the lower bottom half of the screen vertically
player_speed = 1  # Adjust for player movement speed

# Initialize camera variables
camera_x = 0
camera_y = 0

def animate_player():
    global animation_tick, current_player_image
    animation_tick += 1
    if animation_tick >= animation_speed:
        animation_tick = 0
        current_player_image = (current_player_image + 1) % len(player_images)

def draw_visible_background():
    global camera_x, camera_y
    screen.blit(background_img, (0 - camera_x, 0 - camera_y))

def game_loop():
    global player_x, player_y, camera_x, camera_y

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Check for player movement and adjust camera position accordingly
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
            if player_x < SCREEN_WIDTH // 3:
                camera_x -= player_speed
                if camera_x < 0:
                    camera_x = 0
        elif keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed
            if player_x > 2 * SCREEN_WIDTH // 3 - player_width:
                camera_x += player_speed
                if camera_x > background_img.get_width() - SCREEN_WIDTH:
                    camera_x = background_img.get_width() - SCREEN_WIDTH
        elif keys[pygame.K_UP] and player_y > SCREEN_HEIGHT // 4:
            player_y -= player_speed
            if player_y < SCREEN_HEIGHT // 4:
                camera_y -= player_speed
                if camera_y < 0:
                    camera_y = 0
        elif keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT // 2 - player_height:
            player_y += player_speed
            if player_y > SCREEN_HEIGHT // 2 - player_height:
                camera_y += player_speed
                if camera_y > background_img.get_height() - SCREEN_HEIGHT:
                    camera_y = background_img.get_height() - SCREEN_HEIGHT

        screen.fill((0, 0, 0))  # Fill the screen with black

        # Animate player if moving
        if any(keys):
            animate_player()

        # Draw visible portion of background based on camera position
        draw_visible_background()

        # Draw player
        screen.blit(player_images[current_player_image], (player_x, player_y))
        
        pygame.display.update()


if __name__ == "__main__":
    game_loop()
