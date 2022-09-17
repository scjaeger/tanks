import pygame
from src.constants.constants import   FPS, GENERAL_TANK_SETTINGS, LEFT_TANK_SETTINGS, RIGHT_TANK_SETTINGS, BIG_FONT, STAT_FONT, WIN, BLACK, HEIGHT, WHITE, WIDTH
from src.elements.tanks import Tank

class Game():
    def __init__(self):
        self.run = True
        self.finished = False
        self.clock = pygame.time.Clock()
        self.left_tank = Tank(GENERAL_TANK_SETTINGS, *LEFT_TANK_SETTINGS.values())
        self.right_tank = Tank(GENERAL_TANK_SETTINGS, *RIGHT_TANK_SETTINGS.values())
        self.left_tank.enemy = self.right_tank
        self.right_tank.enemy = self.left_tank
        self.window = WIN
        self.fps = FPS
        self.countdown = 1000

    
    def loop(self, decisions = None, frame_limit = True):

        # check if game is closed by pressing the x-button
        self.check_game_quit()

        # limits the game to given frames per second if True
        if frame_limit:
            self.clock.tick(self.fps)
        
        # draw elements on the game window
        self.draw()

        # movement of game elements. If decision by AI else by user
        if decisions:
            for tank, decision in zip([self.left_tank, self.right_tank], decisions):
                self.decide_action(decision, tank)
        else:
            self.handle_controls()
        
        # test if bullets collide with hit boxes
        self.check_hit()

        # check for shields and finish the game if they are gone
        if self.check_win(frame_limit):
            self.finished = True

        self.countdown -= 1

        return None

    def draw(self):
        # draw background
        self.window.fill(BLACK)

        # print timer
        win_text = "countdown = {} ".format(self.countdown)
        text = STAT_FONT.render(win_text, 1, WHITE)
        WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

        # draw tanks
        for tank in [self.left_tank, self.right_tank]:
            tank.draw()

            # draw bullets
            if tank.shots_fired:
                tank.bullet.move()
                tank.bullet.draw()

        # update window
        pygame.display.update()

        return None


    def check_game_quit(self):
        # check if quit button is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        
        return None


    def handle_controls(self):
        # get user-key interactions
        keys = pygame.key.get_pressed()

        for tank in [self.left_tank, self.right_tank]:
            # start action according to pressed keys
            if keys[tank.aim_left]:
                tank.aim(left = True)
            if keys[tank.aim_right]:
                tank.aim(left = False)
            if keys[tank.move_left]:
                tank.move(left=True)
            if keys[tank.move_right]:
                tank.move(left=False)

            elif keys[tank.shoot_button]:
                tank.shoot()
            
            # check if bullet hits ground, then reload
            tank.bullet.check_reset(tank, tank.enemy)

        return None

    
    def check_hit(self):
        for tank in [self.left_tank, self.right_tank]:

            # set hit box
            hit_box = {
                "left": tank.x - 2*tank.top_radius,
                "right": tank.x + 2*tank.top_radius,
                "top": HEIGHT - 2* tank.top_radius
                }
            # check collision of bullet and hit box
            if hit_box["left"] < tank.enemy.bullet.x < hit_box["right"] and tank.enemy.bullet.y > hit_box["top"]:

                # reload and set stats
                tank.enemy.shots_fired = False
                tank.shield -= 1
                tank.enemy.bullet.__init__(self.right_tank.color)


    def check_win(self, frame_limit = True):
        for tank, name in zip([self.left_tank, self.right_tank], ["right", "left"]):

            # check left over shield
            if tank.shield <= 0:

                # print text for winer
                win_text = "{} player is victorious!".format(name)
                text = BIG_FONT.render(win_text, 1, WHITE)
                WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))

                if frame_limit:
                    # pause game to celebrate victory
                    pygame.display.update()
                    pygame.time.delay(3000)
                
                return True

    def decide_action(self, decision, tank):
        # assign actions to ai decisions
        if decision == 0:
            tank.shoot()
        elif decision == 1:
            tank.move(left = True)
        elif decision == 2:
            tank.move(left = False)
        elif decision == 3:
            tank.aim(left = True)
        elif decision == 4:
            tank.aim(left = False)
        tank.bullet.check_reset(tank, tank)