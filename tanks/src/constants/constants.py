import pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")
FPS = 60
FONT = pygame.font.SysFont("comicsans", 50)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# tank design
TOP_RADIUS = 15
LEFT_TANK_START_ANGLE = 45
RIGHT_TANK_START_ANGLE = 135
TANK_X_OFFSET = 100

# tank control
LEFT_TANK_AIM_LEFT = pygame.K_w
LEFT_TANK_AIM_RIGHT = pygame.K_s
LEFT_TANK_MOVE_LEFT = pygame.K_a
LEFT_TANK_MOVE_RIGHT = pygame.K_d
LEFT_TANK_SHOOT = pygame.K_SPACE

RIGHT_TANK_AIM_LEFT = pygame.K_DOWN
RIGHT_TANK_AIM_RIGHT = pygame.K_UP
RIGHT_TANK_MOVE_LEFT = pygame.K_LEFT
RIGHT_TANK_MOVE_RIGHT = pygame.K_RIGHT
RIGHT_TANK_SHOOT = pygame.K_RCTRL

AIM_STEP = 0.02

# bullet settings
BULLET_VELOCITY = 12
BULLET_SIZE = 4
GRAVITY = 0.15