import pygame

BLACK = (0,0,0)
WHITE = (225,225,225)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

player_url = 'd_images/player.png'
player_img = pygame.image.load(player_url)

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()


    screen.blit(player_img,(100,100))

    pygame.display.flip()