import pygame
pygame.init()

width, height = 1920, 1080
size =(width, height)

screen = pygame.display.set_mode(size)
player = pygame.image.load('exresources/image/creeper.png')

while True:
    for event in pygame.event.get():
        screen.fill((0,0,0))
        screen.blit(player, (1000, 500))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


