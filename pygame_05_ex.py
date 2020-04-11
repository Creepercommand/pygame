import pygame

width, height = 900, 675
size = (width, height)
screen = pygame.display.set_mode(size)

bg_image = pygame.image.load('exresources/image/funny.jpg')
go = pygame.image.load('exresources/image/goja.jpg')
korea = pygame.image.load('exresources/image/korea.png')
gong = pygame.image.load('exresources/image/maxresdefault.jpg')
kim = pygame.image.load('exresources/image/maxresdefault (1).jpg')
sang = pygame.image.load('exresources/image/oh.jpg')



while True:
    for x in range(5):
        for y in range(6):
            screen.blit(bg_image,(x*225,y*225))
    screen.blit(korea, (280, 20))
    screen.blit(go,(0,0))
    screen.blit(gong, (0, 200))
    screen.blit(kim, (500, 300))
    screen.blit(sang ,(200,500))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)




