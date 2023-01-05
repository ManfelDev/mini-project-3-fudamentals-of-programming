import math
import pygame

class Bullet(object):
    def __init__(self, player, time):
        self.x = player.x + 25 * math.cos(player.angle)
        self.y = player.y - 25 * math.sin(player.angle)
        self.angle = player.angle
        self.initial_velocity = 50
        self.time = time
        self.g = 9.8
        self.active = True
        self.last_shoot_time = 0
        self.radius = 5
        self.update_collider()
    
    def update_collider(self):
        self.collider = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self):
        self.x += + self.initial_velocity * self.time * math.cos(self.angle)
        self.y -= + self.initial_velocity * self.time * math.sin(self.angle) - 0.5 * self.g * self.time ** 2
        screen_width = 1000
        screen_height = 380
        if self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height:
            self.active = False
        self.update_collider()
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)