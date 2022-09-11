import pygame
import random
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")
FPS = 60
BIG_FONT = pygame.font.SysFont("comicsans", 50)
STAT_FONT = pygame.font.SysFont("comicsans", 25)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# tank settings
GENERAL_TANK_SETTINGS = {
    "top_radius": 15,
    "aim_step": 0.02,
    "bullet_velocity": 12,
    "bullet_size": 4,
    "gravity": 0.15,
    "start_y": HEIGHT,
    "shield": 3
}

LEFT_TANK_SETTINGS = {
    "start_angle": 45 + random.randint(-5, 5),
    "start_x": 100 + random.randint(-70, 70),
    "aim_left": pygame.K_w,
    "aim_right": pygame.K_s,
    "move_left": pygame.K_a,
    "move_right": pygame.K_d,
    "shoot": pygame.K_SPACE,
    "color": WHITE
}

RIGHT_TANK_SETTINGS = {
    "start_angle": 135 + random.randint(-5, 5),
    "start_position": WIDTH - 100 + random.randint(-70, 70),
    "aim_left": pygame.K_DOWN,
    "aim_right": pygame.K_UP,
    "move_left": pygame.K_LEFT,
    "move_right": pygame.K_RIGHT,
    "shoot": pygame.K_RCTRL,
    "color": WHITE
}

