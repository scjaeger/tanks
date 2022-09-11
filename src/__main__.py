import pygame
from src.Game.game import Game
pygame.init()




def main():
    game = Game()

    while game.run:

        game.loop()

        if game.finished:
            main()



    pygame.quit()


if __name__ == "__main__":
    main()
        
