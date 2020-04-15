import pygame

WHITE = (225,225,225)
BLACK = (0,0,0)
RED = (225,0,0)
GREEN = (0,225,0)
BLUE = (0,0,225)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLOCK_SIZE = 20

def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * BLOCK_SIZE, position[1]*BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
block_position = [0,0]

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                block_position[0] += 1
            if event.key == pygame.K_LEFT:
                block_position[0] -= 1
            if event.key == pygame.K_UP:
                block_position[1] -= 1
            if event.key == pygame.K_DOWN:
                block_position[1] += 1




    screen.fill(WHITE)
    draw_block(screen, GREEN, block_position)
    pygame.display.flip()