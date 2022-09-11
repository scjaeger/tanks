from src.constants.constants import GENERAL_TANK_SETTINGS, HEIGHT, WIDTH, WIN
import math
import pygame

class Bullet():
    def __init__(self, color):
        self.size = GENERAL_TANK_SETTINGS["bullet_size"]
        self.x = 0 - self.size
        self.y = 0 - self.size
        self.angle = 0
        self.max_vel = GENERAL_TANK_SETTINGS["bullet_velocity"]
        self.x_vel = 0
        self.y_vel = 0
        self.color = color

    def start_shot(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.x_vel = int(self.max_vel * math.cos(self.angle))
        self.y_vel = int(self.max_vel * math.sin(self.angle) * (-1))

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.size)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.y_vel += GENERAL_TANK_SETTINGS["gravity"]

    def check_reset(self, tank):
        if self.x < 0 or self.x > WIDTH or self.y > HEIGHT:
            self.__init__(self.color)
            tank.shots_fired = False