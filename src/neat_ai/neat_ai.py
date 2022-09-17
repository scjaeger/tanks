from src.game.game import Game
import pygame
import neat
from src.constants.constants import WIN
import math


class NeatGame():
    def __init__(self):
        self.game = Game()
        self.left_tank = self.game.left_tank
        self.right_tank = self.game.right_tank


    

    def train_ai(self, genome1, genome2, config):
        # create two neural networks to play agains each other
        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        net2 = neat.nn.FeedForwardNetwork.create(genome2, config)

        # start game loop
        while self.game.run:
            
            # get outputs of neural networks dependend on input feed
            output_1 = net1.activate((
                # self.left_tank.x, 
                self.left_tank.angle, 
                self.right_tank.x - self.left_tank.x,
                self.right_tank.bullet.x - self.left_tank.x,
                self.right_tank.bullet.y
                ))

            output_2 = net2.activate((
                # self.right_tank.x, 
                self.right_tank.angle, 
                self.left_tank.x - self.right_tank.x,
                self.left_tank.bullet.x - self.right_tank.x,
                self.left_tank.bullet.y
                ))

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
            added_fitness = tank.shield *25
            added_fitness += tank.hits * 100
            #added_fitness += tank.ammo_used
            added_fitness += tank.close_hits


            genome.fitness += added_fitness
            