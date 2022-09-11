import pygame

def check_game_quit(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    return run