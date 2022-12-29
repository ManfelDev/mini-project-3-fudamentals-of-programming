import pygame
import math

cannon = pygame.image.load('images/cannon.png')

class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.length = 25

    def draw(self, screen, color):
        # Draw cannon
        end_x = self.x + self.length * math.cos(self.angle)
        end_y = self.y - self.length * math.sin(self.angle)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y), (end_x, end_y), 5)
        # Draw cannon base
        pygame.draw.rect(screen, color, pygame.Rect(35,215,28,15))
    
    def draw_area(self, screen, color):
        # Draw area
        pygame.draw.rect(screen, color, pygame.Rect(0,230,100,150))
        