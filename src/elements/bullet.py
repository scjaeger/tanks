from src.constants.constants import GENERAL_TANK_SETTINGS, HEIGHT, WIDTH, WIN
import math
import pygame

class Bullet():
    def __init__(self,x, y, angle, color):
        self.size = GENERAL_TANK_SETTINGS["bullet_size"]
        self.x = x
        self.y = y
        self.angle = angle
        self.max_vel = GENERAL_TANK_SETTINGS["bullet_velocity"]
        self.x_vel = int(self.max_vel * math.cos(self.angle))
        self.y_vel = int(self.max_vel * math.sin(self.angle) * (-1))
        self.color = color

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.size)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.y_vel += GENERAL_TANK_SETTINGS["gravity"]

    def check_reset(self, tank_1, tank_2, bullet_id):
        if self.x < 0 or self.x > WIDTH or self.y > HEIGHT:
            del tank_1.bullet[bullet_id]
            close_hit_score = round((5 - abs(tank_2.x - self.x))/10, 0)
            tank_1.close_hits += max(0, close_hit_score)

            