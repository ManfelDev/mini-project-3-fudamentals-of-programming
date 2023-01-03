import pygame

class Enemies(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.points = [(-20, 20), (20, 20), (5, 30), (-5, 30)]
        elif self.rank == 2:
            self.points = [(-25, 20), (25, 20), (10, 30), (-10, 30)]
        elif self.rank == 3:
            self.points = [(-35, 20), (35, 20), (20, 30), (-20, 30)]
        elif self.rank == 4:
            self.points = [(-45, 20), (45, 20), (30, 30), (-30, 30)]
        elif self.rank == 5:
            self.points = [(-55, 20), (55, 20), (40, 30), (-40, 30)]
        self.x = 1100
        self.y = 300
        self.speed = 1
        self.spawn_delay = 2000
        
    def update(self):
        self.x -= self.speed
    
    def draw(self, surface):
        points = [(x + self.x, y + self.y) for x, y in self.points]
        pygame.draw.polygon(surface, (255, 0, 0), points, 0)

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