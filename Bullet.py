import math
import pygame

class Bullet(object):
    def __init__(self, player, time):
        self.x = player.x + 25 * math.cos(player.angle)
        self.y = player.y - 25 * math.sin(player.angle)
        self.angle = player.angle
        self.time = time
        self.tupdate = 0
        self.initial_velocity = 1000 * self.time
        self.g = 9.8
        self.vx = self.initial_velocity * math.cos(self.angle)
        self.vy = self.initial_velocity * math.sin(self.angle)
        self.drag_coefficient = 0.001
        self.active = True
        self.last_shoot_time = 0
        self.radius = 5
        self.update_collider()
    
    def update_collider(self):
        self.collider = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def update(self, framerate):
        self.tupdate = 1 / framerate
        # Calculate the acceleration due to drag
        drag_x = -self.drag_coefficient * self.vx ** 2
        drag_y = -self.drag_coefficient * self.vy ** 2
        # Update the bullet's velocity based on the acceleration due to gravity and drag
        self.vx += drag_x * self.tupdate
        self.vy -= (self.g + drag_y) * self.tupdate
        # Update the bullet's position based on its velocity
        self.x += self.vx * self.tupdate
        self.y -= self.vy * self.tupdate
        screen_width = 1000
        screen_height = 380
        if self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height:
            self.active = False
        self.update_collider()
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)