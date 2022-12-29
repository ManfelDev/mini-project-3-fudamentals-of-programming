import pygame

class Enemies(object):
    def danger_zone(self, screen, color):
        self.draw_area = pygame.draw.rect(screen, color, pygame.Rect(100,330,100,50))
    def enemy_zone(self, screen, color):
        self.draw_area = pygame.draw.rect(screen, color, pygame.Rect(200,330,800,50))