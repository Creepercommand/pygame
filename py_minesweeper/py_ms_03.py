#03. 타일 클릭처리

import pygame
from random import randint

COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
NUM_OF_BOMS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
game_over = False
BALCK = (0,0,0)
GRAY_LINE = (100,100,100)
GRAY_TITLE = (200,200,200)
YELLOW_BOMB = (255,255,0)
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('py mine sweeper')

filed = [[EMPTY for x_col in range(COL_COUNT)] for y_row in range(ROW_COUNT)]

count = 0
while count < NUM_OF_BOMS:
    x_col, y_row = randint(0, COL_COUNT -1), randint(0, ROW_COUNT -1)
    if filed[y_row][x_col] == EMPTY:
        filed[y_row][x_col] = BOMB
        count += 1

running = True
#메인 루프
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_col = event.pos[0] // CELL_SIZE
            y_row = event.pos[1] // CELL_SIZE
            if filed[y_row][x_col] == BOMB:
                game_over = True
                print('게임 오버')

    screen.fill(BALCK)

    for y_row in range(ROW_COUNT):
        for x_col in range(COL_COUNT):
            tile = filed[y_row][x_col]
            rect = (x_col * CELL_SIZE, y_row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if tile == EMPTY or BOMB:
                pygame.draw.rect(screen, GRAY_TITLE, rect)
            if game_over == True and tile == BOMB:
                pygame.draw.ellipse(screen, YELLOW_BOMB, rect)

    for idx in range(0, COL_COUNT * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, GRAY_LINE, (idx, 0), (idx, ROW_COUNT * CELL_SIZE))
    for idx in range(0, ROW_COUNT * CELL_SIZE, CELL_SIZE):
        pygame.draw.line(screen, GRAY_LINE, (0, idx), (COL_COUNT * CELL_SIZE, idx))


    pygame.display.update()

pygame.quit()
print(filed)