import pygame
from src.game.game import Game
from src.neat_ai.neat_ai import NeatGame
import neat
pygame.init()




def main():
    game = Game()

    while game.run:

        game.loop()

        print(game.left_tank.bullet)

        if game.finished:
            main()



    pygame.quit()




if __name__ == "__main__":
    # main()

    
    
    ai_game = NeatGame()
    ai_game.run_neat()
        
