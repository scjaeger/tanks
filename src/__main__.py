import pygame
from src.game.game import Game
from src.neat_ai.neat_ai import NeatGame
import neat
pygame.init()




def main():
    game = Game()

    while game.run:

        game.loop()

        if game.finished:
            main()



    pygame.quit()

def eval_genomes(genomes,  config):


        for i, (genome_id1, genome1) in enumerate(genomes):
            if i ==len(genomes) -1:
                break
            genome1.fitness = 0
            for genome_id2, genome2 in genomes[i+1:]:
                genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
                game = NeatGame()
                game.train_ai(genome1, genome2, config)
    
def run_neat(config):
    pop = neat.Population(config)
    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(1))

    winner = pop.run(eval_genomes, 50)


if __name__ == "__main__":
    # main()

    config_path = "src/neat_ai/config.txt"
    config = neat.Config(
        neat.DefaultGenome, 
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
        )
    
    run_neat(config)
        
