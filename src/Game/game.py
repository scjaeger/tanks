import pygame
from src.constants.constants import   FPS, GENERAL_TANK_SETTINGS, LEFT_TANK_SETTINGS, RIGHT_TANK_SETTINGS, BIG_FONT, WIN, BLACK, HEIGHT, WHITE, WIDTH
from src.elements.tanks import Tank

class Game():
    def __init__(self):
        self.run = True
        self.finished = False
        self.clock = pygame.time.Clock()
        self.left_tank = Tank(GENERAL_TANK_SETTINGS, *LEFT_TANK_SETTINGS.values())
        self.right_tank = Tank(GENERAL_TANK_SETTINGS, *RIGHT_TANK_SETTINGS.values())
        self.window = WIN
        self.fps = FPS

    
    def loop(self):
        self.check_game_quit()

        self.clock.tick(self.fps)
        
        self.draw()

        self.handle_controls()
        
        self.check_hit()

        if self.check_win():
            self.finished = True

        print("left: {}, right: {}".format(self.left_tank.performace, self.right_tank.performace))

        return None

    def draw(self):
        self.window.fill(BLACK)
        for tank in [self.left_tank, self.right_tank]:
            tank.draw()
            if tank.shots_fired:
                tank.bullet.draw()
        pygame.display.update()

        return None


    def check_game_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        
        return None


    def handle_controls(self):
        keys = pygame.key.get_pressed()
        for tank in [self.left_tank, self.right_tank]:
            tank.aim(keys)
            tank.move(keys)
            if tank.shots_fired:
                tank.bullet.move()
            else:
                tank.shoot(keys)
            tank.bullet.check_reset(tank)

        return None

    
    def check_hit(self):
        for left in [True, False]:
            if left:
                tank_1 = self.left_tank
                tank_2 = self.right_tank
            else:
                tank_1 = self.right_tank
                tank_2 = self.left_tank

            hit_box = {
                "left": tank_1.x - 2*tank_1.top_radius,
                "right": tank_1.x + 2*tank_1.top_radius,
                "top": HEIGHT - 2* tank_1.top_radius
                }
            if hit_box["left"] < tank_2.bullet.x < hit_box["right"] and tank_2.bullet.y > hit_box["top"]:
                tank_2.performace += 5
                tank_2.shots_fired = False
                tank_1.shield -= 1
                tank_1.performace -= 2
                tank_2.bullet.__init__(self.right_tank.color)


    def check_win(self):
        for tank, name in zip([self.left_tank, self.right_tank], ["right", "left"]):
            if tank.shield <= 0:
                win_text = "{} player is victorious!".format(name)
                text = BIG_FONT.render(win_text, 1, WHITE)
                WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
                pygame.display.update()
                pygame.time.delay(3000)
                
                return True