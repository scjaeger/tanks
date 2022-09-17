from src.game.game import Game
import pygame
import neat
from src.constants.constants import WIDTH, HEIGHT, CONFIG_PATH
import math


class NeatGame():
    def __init__(self):
        self.game = Game()
        self.left_tank = self.game.left_tank
        self.right_tank = self.game.right_tank
        self.config = self.set_config()


    def set_config(self):
        config_path = CONFIG_PATH
        config = neat.Config(
            neat.DefaultGenome, 
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path
            )

        return config

    def eval_genomes(self, genomes,  config):

        for i, (genome_id1, genome1) in enumerate(genomes):
            if i ==len(genomes) -1:
                break
            genome1.fitness = 0
            for genome_id2, genome2 in genomes[i+1:]:
                genome2.fitness = 0 if genome2.fitness == None else genome2.fitness
                game = NeatGame()
                game.train_ai(genome1, genome2, config)
    
    def run_neat(self, config):
        pop = neat.Population(config)
        pop.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        pop.add_reporter(stats)
        pop.add_reporter(neat.Checkpointer(1))

        winner = pop.run(self.eval_genomes, 50)
    

    def train_ai(self, genome1, genome2, config):
        # create two neural networks to play agains each other
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        # start game loop
        while self.game.run:
            
            # get outputs of neural networks dependend on input feed

            output_1 = net1.activate(self.get_nn_inputs(self.left_tank))

            output_2 = net2.activate(self.get_nn_inputs(self.right_tank))

            # get decision by index of highest activation of output
            decision_1 = output_1.index(max(output_1))
            decision_2 = output_2.index(max(output_2))

            # go through basic game steps
            self.game.loop([decision_1, decision_2], frame_limit = False)

            # end game if manually quitted
            if not self.game.run:
                quit()

            # end game if one side has won or timer is down to 0
            if self.game.check_win(frame_limit = False) or self.game.countdown <= 0:
                self.calculate_fitness(genome1, genome2)
                break

    def calculate_fitness(self, genome1, genome2):
        # add points to fitness score
        for genome, tank in zip([genome1, genome2], [self.left_tank, self.right_tank]):
            added_fitness = tank.shield
            added_fitness += tank.hits * 10
            added_fitness += tank.close_hits


            genome.fitness += added_fitness
            print(genome.fitness)
            

    def get_nn_inputs(self, tank):
        angle = tank.angle
        tank_distance = tank.enemy.x - tank.x
        if len(tank.enemy.bullet) >= 1:
            bullet_distance = tank.enemy.bullet[0].x - tank.x
            bullet_height = tank.enemy.bullet[0].y
        else:
            bullet_distance = WIDTH * 2
            bullet_height = HEIGHT * 2

        return angle, tank_distance, bullet_distance, bullet_height


    