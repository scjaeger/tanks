import pygame

def handle_controls(left_tank, left_bullet, right_tank, right_bullet):
    keys = pygame.key.get_pressed()
    for tank, bullet in zip([left_tank, right_tank], [left_bullet, right_bullet]):
        tank.aim(keys)
        tank.move(keys)
        if tank.shots_fired:
            bullet.move()
        else:
            tank.shoot(keys, bullet)
        bullet.check_reset(tank)