import pygame

class Enemies(object):
    pass

class Danger_Zone(object):
    def __init__(self):
        self.x = 100
        self.y = 330
        self.width, self.height = 100, 50
        
    def draw_zone(self, screen, color):
        self.draw_area = pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y,self.width,self.height))

class Enemy_Zone(object):        
    def __init__(self):
        self.x = 200
        self.y = 330
        self.width, self.height = 800, 50
        
    def draw_zone(self, screen, color):
        self.draw_area = pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y,self.width,self.height))