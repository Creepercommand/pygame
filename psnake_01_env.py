# psnake_01_env.py
# 2020.07.11

import pygame

# 파이게임 초기화
pygame.init()

# 파이게임 화면 만들기
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("pysnake")

#변수 초기화
GRAY = (120,120,120)
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

# 게임 루프
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    #화면 격자 그리기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx * CELL_SIZE ,r_idx * CELL_SIZE ,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,GRAY,one_rect,1)
    pygame.display.update()

pygame.quit()
