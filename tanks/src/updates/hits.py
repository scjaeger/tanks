from src.constants.constants import FONT, WHITE, HEIGHT, WIDTH, WIN
import pygame


def check_hit(bullet, tank, player_name):
    tank_left = tank.x - 2*tank.top_radius
    tank_right = tank.x + 2*tank.top_radius
    tank_height = HEIGHT - 2*tank.top_radius
    if tank_left < bullet.x < tank_right and bullet.y > tank_height:
        win_text = "{} player is victorious!".format(player_name)
        text = FONT.render(win_text, 1, WHITE)
        WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)

        return True
    
    else:
        return False