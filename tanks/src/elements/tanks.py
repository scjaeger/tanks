import pygame
import math
from src.constants.constants import AIM_STEP, WHITE, WIDTH, WIN

class Tank:
    color = WHITE

    def __init__(self, x, y, top_radius, angle, left_aim_button, right_aim_button, shoot_button, move_left, move_right):
        self.x = x
        self.y = y - top_radius
        self.top_radius = top_radius

        self.angle = math.radians(angle)
        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)

        self.aim_left = left_aim_button
        self.aim_right = right_aim_button
        self.shoot_button = shoot_button
        self.shots_fired = False

        self.move_left = move_left
        self.move_right = move_right

        if self.x < WIDTH // 2:
            self.left_limit = 2*self.top_radius
            self.right_limit = WIDTH // 3
        else:
            self.left_limit = 2*WIDTH // 3
            self.right_limit = WIDTH - 2*self.top_radius


    def move(self, keys):
        if keys[self.move_left] and self.x >self.left_limit:
            self.x -= 1
        elif keys[self.move_right] and self.x < self.right_limit:
            self.x += 1


    def shoot(self, keys, bullet):
        if keys[self.shoot_button] and not self.shots_fired:
            bullet.start_shot(self.pipe_x, self.pipe_y, self.angle)
            self.shots_fired = True

    def aim(self, keys):
        if keys[self.aim_left] and  self.angle < math.pi:
            self.angle += AIM_STEP
        elif keys[self.aim_right] and  self.angle > 0:
            self.angle -= AIM_STEP   

        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.top_radius)
        pygame.draw.rect(WIN, self.color, (self.x - 2*self.top_radius, self.y , 4*self.top_radius, self.top_radius))
        pygame.draw.line(WIN, self.color, (self.x, self.y), (self.pipe_x, self.pipe_y), width = self.top_radius // 2)

