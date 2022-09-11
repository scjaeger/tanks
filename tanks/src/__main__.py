import pygame
from src.constants.constants import     FPS, HEIGHT, LEFT_TANK_AIM_LEFT, LEFT_TANK_AIM_RIGHT, LEFT_TANK_MOVE_LEFT, LEFT_TANK_MOVE_RIGHT, LEFT_TANK_SHOOT, LEFT_TANK_START_ANGLE,\
                                        RIGHT_TANK_AIM_LEFT, RIGHT_TANK_AIM_RIGHT, RIGHT_TANK_MOVE_LEFT, RIGHT_TANK_MOVE_RIGHT, RIGHT_TANK_SHOOT, RIGHT_TANK_START_ANGLE, \
                                        TANK_X_OFFSET, WIDTH, WIN, TOP_RADIUS
from src.elements.tanks import Tank
from src.elements.bullet import Bullet
from src.updates.quit_game import check_game_quit
from src.updates.draw import draw
from src.updates.hits import check_hit
from src.updates.controls import handle_controls
pygame.init()




def main():
    run = True
    clock = pygame.time.Clock()

    left_tank = Tank(TANK_X_OFFSET, HEIGHT, TOP_RADIUS, LEFT_TANK_START_ANGLE, LEFT_TANK_AIM_LEFT, LEFT_TANK_AIM_RIGHT, LEFT_TANK_SHOOT, LEFT_TANK_MOVE_LEFT, LEFT_TANK_MOVE_RIGHT)
    left_bullet = Bullet()
    right_tank = Tank(WIDTH - TANK_X_OFFSET, HEIGHT, TOP_RADIUS, RIGHT_TANK_START_ANGLE, RIGHT_TANK_AIM_LEFT, RIGHT_TANK_AIM_RIGHT, RIGHT_TANK_SHOOT, RIGHT_TANK_MOVE_LEFT, RIGHT_TANK_MOVE_RIGHT)
    right_bullet = Bullet()

    while run:
        clock.tick(FPS)
        draw(WIN, left_tank, left_bullet, right_tank, right_bullet)

        run = check_game_quit(run)

        handle_controls(left_tank, left_bullet, right_tank, right_bullet)
        
        if check_hit(left_bullet, right_tank, 'left'):
            main()
        if check_hit(right_bullet, left_tank, 'right'):
            main()



    pygame.quit()


if __name__ == "__main__":
    main()
        
