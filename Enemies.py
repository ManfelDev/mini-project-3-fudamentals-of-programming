import pygame

class Enemies(object):
    def __init__(self, rank):
        self.rank = rank
        if self.rank == 1:
            self.points = [(-20, 20), (20, 20), (5, 30), (-5, 30)]
            self.score = 5
        elif self.rank == 2:
            self.points = [(-25, 20), (25, 20), (10, 30), (-10, 30)]
            self.score = 4
        elif self.rank == 3:
            self.points = [(-35, 20), (35, 20), (20, 30), (-20, 30)]
            self.score = 3
        elif self.rank == 4:
            self.points = [(-45, 20), (45, 20), (30, 30), (-30, 30)]
            self.score = 2
        elif self.rank == 5:
            self.points = [(-55, 20), (55, 20), (40, 30), (-40, 30)]
            self.score = 1
        self.x = 1100
        self.y = 301
        self.speed = 1
        self.spawn_delay = 2000
        self.update_collider()
    
    def update_collider(self):
        min_x = min(self.points, key=lambda x: x[0])[0]
        max_x = max(self.points, key=lambda x: x[0])[0]
        min_y = min(self.points, key=lambda x: x[1])[1]
        max_y = max(self.points, key=lambda x: x[1])[1]
        self.collider = pygame.Rect(self.x + min_x, self.y + min_y, max_x - min_x, max_y - min_y)
        
    def update(self):
        self.x -= self.speed
        self.update_collider()
    
    def draw(self, screen, color):
        points = [(x + self.x, y + self.y) for x, y in self.points]
        pygame.draw.polygon(screen, color, points, 0)
        
    def reset(self):
        # Reset the enemies object to its original state
        self.__init__(self.rank)

class Danger_Zone(object):
    def __init__(self):
        self.x = 100
        self.y = 330
        self.width, self.height = 100, 50
        self.collider = pygame.Rect(0, self.y, self.width, self.height)
        
    def draw_zone(self, screen, color):
        self.draw_area = pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y,self.width,self.height))

class Enemy_Zone(object):
    def __init__(self):
        self.x = 200
        self.y = 330
        self.width, self.height = 800, 50
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def draw_zone(self, screen, color):
        self.draw_area = pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y,self.width,self.height))