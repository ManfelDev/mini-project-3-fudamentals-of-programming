class Player(object):
    def __init__(self):
        self.x = 48
        self.y = 215
        self.angle = 0
    def update(self):
        # Mouse input
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(self.y - mouse_y, mouse_x - self.x)
        self.angle = min(max(angle, -math.pi/15), math.pi/2.5)

class Bullet(object):
    def __init__(self, player, time):
        self.x = player.x + 25 * math.cos(player.angle)
        self.y = player.y - 25 * math.sin(player.angle)
        self.angle = player.angle
        self.initial_velocity = 50
        self.time = time
        self.g = 9.8
    def update(self):
        self.x += + self.initial_velocity * self.time * math.cos(self.angle)
        self.y -= + self.initial_velocity * self.time * math.sin(self.angle) - 0.5 * self.g * (self.time ** 2)