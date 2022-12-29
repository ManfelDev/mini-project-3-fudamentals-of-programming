import pygame
from Player import *
from Enemies import *

# Setting the window
pygame.init()
screen = pygame.display.set_mode((1000, 380))

# Caption
pygame.display.set_caption("Heavy Ordnance")

# Window stuff
screen_center_x = screen.get_width()/2
screen_center_y = screen.get_height()/2
screen_width = screen.get_width()
screen_height = screen.get_height()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255,165,0)
SKY_BLUE = (0,181,226)
GREEN = (75,139,59)
ORANGE = (249,146,69)
OCEAN_BLUE = (0,94,184)
RED = (255,0,0)

# Setting clock
clock = pygame.time.Clock()

# Calling essential stuff
player = Player(48, 215)
enemies = Enemies()

# Start Screen
def startScreen():
    # Create font objects
    font = pygame.font.Font(None, 50)
    title_font = pygame.font.Font(None, 100)
    
    # Create text labels for the tile, the start button and the exit button
    title_text = title_font.render("HEAVY ORDNANCE", True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (screen_center_x, screen_center_y - 130)
    start_text = font.render("START", True, WHITE)
    start_rect = start_text.get_rect()
    start_rect.center = (screen_center_x, screen_center_y)
    exit_text = font.render("EXIT", True, WHITE)
    exit_rect = exit_text.get_rect()
    exit_rect.center = (screen_center_x, screen_center_y + 50)
    
    #Setting the loop to the start screen
    selected_button = "start"  # Start with the start button selected
    while True:
        # Draw the start and exit buttons on the screen
        screen.fill(SKY_BLUE)
        screen.blit(title_text, title_rect)
        if selected_button == "start":
            screen.blit(font.render("START", True, ORANGE), start_rect)
            screen.blit(exit_text, exit_rect)
        else:
            screen.blit(start_text, start_rect)
            screen.blit(font.render("EXIT", True, ORANGE), exit_rect)

        # Wait for a keyboard event
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            # Highligh the selected button
            if event.key == pygame.K_UP:
                # Highlight the start button
                selected_button = "start"
            elif event.key == pygame.K_DOWN:
                # Highlight the exit button
                selected_button = "exit"
            
            # Pressed a button
            if selected_button == "start":
                # If start is pressed
                if event.key == pygame.K_RETURN:
                    break
            elif selected_button == "exit":
                # If Exit is pressed
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    exit()
        
        pygame.display.flip()
        
# Game Screen
def game_Screen():
    # Check if player is alive
    alive = True
    while alive:
        # Updating the score
        # Set FPS
        clock.tick(60)
        
        # If the player wants to close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                exit()
                
        # Mouse input
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(player.y - mouse_y, mouse_x - player.x)
        player.angle = min(max(angle, 0), math.pi/2.5)
                
        # Clear the screen
        screen.fill(SKY_BLUE)
        # Player's area
        player.draw_area(screen, GREEN)
        # Danger zone
        enemies.danger_zone(screen, ORANGE)
        # Enemy Zone
        enemies.enemy_zone(screen, OCEAN_BLUE)
        # Player Draw
        player.draw(screen, BLACK)
                
        # Update the screen
        pygame.display.flip()
        
# Main game loop
while True:
    # Start Screen
    startScreen()
    # Game Screen
    game_Screen()