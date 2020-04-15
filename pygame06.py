import pygame

BLACK = (0,0,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
player_pos = [100,100]
while True:

    screen.fill(BLACK)

    for bx in range(SCREEN_WIDTH // grass.get_width() + 1):
        for by in range(SCREEN_HEIGHT // grass.get_height() + 1):
            screen.blit(grass, (bx * grass.get_width() ,by * grass.get_height()))

    for cy in range(SCREEN_HEIGHT // castle.get_height()):
        screen.blit(castle,(0,30 + cy * castle.get_height()))

    screen.blit(player, player_pos)

    pygame.display.flip()
