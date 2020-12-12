# 도형 연습 파일
#
# py_rect.py

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (10, 20, 100, 50))
    pygame.draw.rect(screen, (255, 0, 0), (150, 10, 100, 30), 3)

    pygame.draw.rect(screen, (0, 255, 0), (100, 80, 80, 50))

    pygame.draw.rect(screen, (0, 0, 255), (200, 60, 140, 80))
    pygame.draw.rect(screen, (255, 225, 0), (30, 160, 100, 50))

    pygame.display.update()
