import pygame
import math
from src.constants.constants import WIDTH, WIN, WHITE, HEIGHT, STAT_FONT
from src.elements.bullet import Bullet

class Tank:

    def __init__(self, GENERAL_TANK_SETTINGS, angle, x, left_aim_button, right_aim_button, move_left_button, move_right_button, shoot_button, color):
        
        # appearance
        self.angle = math.radians(angle)
        self.top_radius = GENERAL_TANK_SETTINGS["top_radius"]
        self.y = GENERAL_TANK_SETTINGS["start_y"] - self.top_radius
        self.x = x
        self.color = color
        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)

        # controls
        self.aim_step = GENERAL_TANK_SETTINGS["aim_step"]
        self.aim_left = left_aim_button
        self.aim_right = right_aim_button
        self.shoot_button = shoot_button
        self.shots_fired = False
        self.bullet = Bullet(self.color)
        self.move_left = move_left_button
        self.move_right = move_right_button

        # performance
        self.performace = 10
        self.shield = GENERAL_TANK_SETTINGS["shield"]

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


    def shoot(self, keys):
        if keys[self.shoot_button] and not self.shots_fired:
            self.bullet.start_shot(self.pipe_x, self.pipe_y, self.angle)
            self.performace -= 1
            self.shots_fired = True

    def aim(self, keys):
        if keys[self.aim_left] and  self.angle < math.pi:
            self.angle += self.aim_step
        elif keys[self.aim_right] and  self.angle > 0:
            self.angle -= self.aim_step   

        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.top_radius)
        pygame.draw.rect(WIN, self.color, (self.x - 2*self.top_radius, self.y , 4*self.top_radius, self.top_radius))
        pygame.draw.line(WIN, self.color, (self.x, self.y), (self.pipe_x, self.pipe_y), width = self.top_radius // 2)

        shield_text = "Shield: {}".format(self.shield)
        text = STAT_FONT.render(shield_text, 1, WHITE)
        WIN.blit(text, (self.left_limit + 100 - text.get_width()//2, HEIGHT//4 - text.get_height()//2))

