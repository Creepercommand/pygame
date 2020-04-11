#파이게임 이미지 처리

import pygame

width, height = 640,480
size = (width, height)
screen = pygame.display.set_mode(size)


player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')

while True:
    screen.fill((0,0,0))

    #토기 이미지 그리기
    grass_width = grass.get_width()
    grass_height = grass.get_height()

    for y in range(height // grass_height+1):
        for x in range(width // grass_width+1):
            screen.blit(grass,((x*grass_width),(y*grass_height)))

    castle_height = castle.get_height()

    for y in range(height// castle_height):
        screen.blit(castle, (0,30 +y * castle_height))
    screen.blit(player, (100, 100))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)