import pygame
import math
from src.constants.constants import GENERAL_TANK_SETTINGS, WIDTH, WIN, WHITE, HEIGHT, STAT_FONT
from src.elements.bullet import Bullet
import random

class Tank:

    def __init__(self, GENERAL_TANK_SETTINGS, angle, x, left_aim_button, right_aim_button, move_left_button, move_right_button, shoot_button, color):
        
        # appearance
        self.angle = math.radians(angle[0] + random.randint(-angle[1], angle[1]))
        self.top_radius = GENERAL_TANK_SETTINGS["top_radius"]
        self.y = GENERAL_TANK_SETTINGS["start_y"] - self.top_radius
        self.x = x[0] + random.randint(-x[1], x[1])
        self.color = color
        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)

        # controls
        self.aim_step = GENERAL_TANK_SETTINGS["aim_step"]
        self.aim_left = left_aim_button
        self.aim_right = right_aim_button
        self.shoot_button = shoot_button
        self.reload = 0
        self.bullet =   []
        self.move_left = move_left_button
        self.move_right = move_right_button

        # game
        self.enemy = None


        # performance 
        self.shield = GENERAL_TANK_SETTINGS["shield"]
        self.hits = 0
        self.close_hits = 0

        if self.x < WIDTH // 2:
            self.left_limit = 2*self.top_radius
            self.right_limit = WIDTH // 3
        else:
            self.left_limit = 2*WIDTH // 3
            self.right_limit = WIDTH - 2*self.top_radius


    def move(self, left = True):
        if left and self.x >self.left_limit:
            self.x -= 1

        elif not left and self.x < self.right_limit:
            self.x += 1

        else:
            pass
        
        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)


    def shoot(self):
        if self.reload <= 0:
            self.bullet.append(Bullet(self.pipe_x, self.pipe_y, self.angle,self.color))
            self.reload = GENERAL_TANK_SETTINGS["reload time"]


    def aim(self, left = True):
        if left and self.angle < math.pi:
            self.angle += self.aim_step
        elif not left and self.angle > 0:
            self.angle -= self.aim_step 
        else:
            pass  

        self.pipe_x = int(self.x + math.cos(self.angle) * 2 * self.top_radius)
        self.pipe_y = int(self.y - math.sin(self.angle) * 2 * self.top_radius)

    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.top_radius)
        pygame.draw.rect(WIN, self.color, (self.x - 2*self.top_radius, self.y , 4*self.top_radius, self.top_radius))
        pygame.draw.line(WIN, self.color, (self.x, self.y), (self.pipe_x, self.pipe_y), width = self.top_radius // 2)

        shield_text = "Shield: {}".format(self.shield)
        text = STAT_FONT.render(shield_text, 1, WHITE)
        WIN.blit(text, (self.left_limit + 100 - text.get_width()//2, HEIGHT//4 - text.get_height()//2))

