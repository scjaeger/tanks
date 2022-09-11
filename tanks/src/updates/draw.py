from src.constants.constants import BLACK
import pygame



def draw(win, left_tank, left_bullet, right_tank, right_bullet):
    win.fill(BLACK)
    for tank, bullet in zip([left_tank, right_tank], [left_bullet, right_bullet]):
        tank.draw()
        if tank.shots_fired:
            bullet.draw()
    pygame.display.update()