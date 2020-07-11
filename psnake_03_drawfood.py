# psnake_03_drawfood
# 먹이 그리기
# 화면 무작위로 먹이 10개 그리기
# 화면에 무작위로 뱀 위치나 이전먹이 위치에 그릴수 없다.

import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")

GRAY = (120,120,120)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

bodies = [(COL_COUNT // 2,ROW_COUNT//2)]

foods = []
for _ in range(10):
    while True:
        c_idx = random.randint(0,COL_COUNT -1)
        r_idx = random.randint(0,ROW_COUNT -1)
        f_pos = (c_idx,r_idx)
        #중복 확인
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx * CELL_SIZE , r_idx* CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 1)
    #먹이 그리기
    for one in foods:
        f_rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE, CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(screen,WHITE,f_rect)


    for one in bodies:
        b_rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE, CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(screen,BLUE,b_rect)

        pygame.display.update()

pygame.quit()
