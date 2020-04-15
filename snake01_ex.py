import pygame
import time

WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
GREEN = (0, 225, 0)
BULE = (0, 0, 255)

WIDTH = 600
HEIGHT = 300
SCREEN_SIZE = (WIDTH, HEIGHT)
BLOCK_SIZE = 10


def draw_block(screen, color, position):
    x = position[0]
    y = position[1]
    block_rect = pygame.Rect((x * BLOCK_SIZE, y * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block_rect)


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

for bx in range(0, WIDTH // BLOCK_SIZE + 1, 2):
    for by in range(0, HEIGHT // BLOCK_SIZE + 1, 2):
        draw_block(screen, GREEN, (bx, by))
        draw_block(screen, RED, (bx+1, by))
        draw_block(screen, RED, (bx, by+1))
        draw_block(screen, GREEN, (bx +1 , by +1))
        time.sleep(0.01)
        pygame.display.flip()





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
