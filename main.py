import pygame
from Player import *
from Enemies import *
from Bullet import *

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
enemy_zone = Enemy_Zone()
danger_zone = Danger_Zone()
bullets = []

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
    # Set up a variable to store the time when the key is first pressed
    key_press_time = 0
    # Set the minimum time between actions in seconds
    MIN_TIME_BETWEEN_ACTIONS = 1
    # Set the time of the last action to 0
    last_action_time = 0
    # Check if player is alive
    alive = True
    
    while alive:
        # Set FPS
        clock.tick(60)  
        
        # Bullets Update
        for b in bullets:
            b.update()
            # Check if the bullet is out of bounds
            if b.active == False:
                bullets.pop(bullets.index(b))
            # Check if the bullet collides with the enemy zone
            rect_b_ezone = pygame.Rect(enemy_zone.x, enemy_zone.y, enemy_zone.width, enemy_zone.height)
            if rect_b_ezone.colliderect(b.x - b.radius, b.y - b.radius, b.radius * 2, b.radius * 2):
                bullets.pop(bullets.index(b))
        
        # Check for events (inputs)
        for event in pygame.event.get():
            # If the player wants to close the game
            if event.type == pygame.QUIT:
                # Quit the game and close the window
                pygame.quit() 
                exit()
            # If the player presses the mouse button
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the current time
                key_press_time = pygame.time.get_ticks()
            # If the player releases the mouse button
            elif event.type == pygame.MOUSEBUTTONUP:
                # Get the current time
                current_time = pygame.time.get_ticks()
                # Calculate the elapsed time between the press and release of the mouse button
                elapsed_time = (current_time - key_press_time) / 1000
                # Calculate the elapsed time since the last action
                action_elapsed_time = (current_time - last_action_time) / 1000
                # If the elapsed time since the last action is greater than or equal to the minimum time between actions
                if action_elapsed_time >= MIN_TIME_BETWEEN_ACTIONS:
                    # Store the current time as the time of the last action
                    last_action_time = current_time
                    # Check if theres less than 2 bullets on the field
                    if len(bullets) < 2:
                        if elapsed_time != 0:
                            if elapsed_time < 0.7:
                                bullets.append(Bullet(player, elapsed_time))
                            if elapsed_time >= 0.7:
                                elapsed_time = 0.7
                                bullets.append(Bullet(player, elapsed_time))
                    else:
                        pass
                    
        # Player Update
        player.update()
        # Clear the screen
        screen.fill(SKY_BLUE)
        # Player's area
        player.draw_area(screen, GREEN)
        # Danger zone
        danger_zone.draw_zone(screen, ORANGE)
        # Enemy Zone
        enemy_zone.draw_zone(screen, OCEAN_BLUE)
        # Player Draw
        player.draw(screen, BLACK)
        # Bullet Draw
        for b in bullets:
            b.draw(screen, BLACK)
                
        # Update the screen
        pygame.display.flip()
        
# Main game loop
while True:
    # Start Screen
    startScreen()
    # Game Screen
    game_Screen()