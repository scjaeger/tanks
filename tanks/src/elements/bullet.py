from src.constants.constants import BULLET_SIZE, BULLET_VELOCITY, GRAVITY, HEIGHT, WHITE, WIDTH, WIN
import math
import pygame

class Bullet():
    color = WHITE

    def __init__(self):
        self.x = WIDTH + BULLET_SIZE
        self.y = HEIGHT + BULLET_SIZE
        self.angle = 0
        self.x_vel = 0
        self.y_vel = 0

    def start_shot(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.x_vel = int(BULLET_VELOCITY * math.cos(self.angle))
        self.y_vel = int(BULLET_VELOCITY * math.sin(self.angle) * (-1))

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), BULLET_SIZE)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.y_vel += GRAVITY

    def check_reset(self, tank):
        if self.x < 0 or self.x > WIDTH or self.y > HEIGHT:
            self.__init__()
            tank.shots_fired = False