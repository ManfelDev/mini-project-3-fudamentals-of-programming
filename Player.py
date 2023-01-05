import pygame
import math

class Player(object):
    def __init__(self):
        self.x = 48
        self.y = 215
        self.angle = 0
        self.length = 25
        self.score = 0
        self.lives = 3
        self.start_time = pygame.time.get_ticks()

    def update(self):
        # Mouse input
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(self.y - mouse_y, mouse_x - self.x)
        self.angle = min(max(angle, -math.pi/15), math.pi/2.5)
        
    def increase_score(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        if elapsed_time > 1000:  # If more than 1 second has passed
            self.score += 1  # Increase the score by 1
            self.start_time = pygame.time.get_ticks()  # Reset the start 

    def draw(self, screen, color):
        # Draw cannon
        end_x = self.x + self.length * math.cos(self.angle)
        end_y = self.y - self.length * math.sin(self.angle)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (end_x, end_y), 5)
        # Draw cannon base
        pygame.draw.rect(screen, color, pygame.Rect(35,215,28,15))
        
    def draw_lifes(self, screen, heart_image):
        x = 955
        y = 35
        for i in range(self.lives):
            screen.blit(heart_image, (x, y))
            x -= 25  # Decrement the x position for the next heart
    
    def draw_area(self, screen, color):
        # Draw area
        pygame.draw.rect(screen, color, pygame.Rect(0,230,100,150))
        
    def reset(self):
        # Reset the player object to its original state
        self.__init__()