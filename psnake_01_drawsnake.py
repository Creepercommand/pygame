# psnake_02_drawsnake.py
# 뱀 몸통 그리기
# bodies[]: 뱀 좌표를 튜플로 보관하는 리스트
# bodies[(x1,y1),(x2,y2),....]

import pygame

#화면 설정
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")

#변수 초기화
GRAY = (120,120,120)
BLUE = (0,0,255)
BLACK = (0,0,0)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

bodies = [(COL_COUNT//2,ROW_COUNT//2)]
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    screen.fill(BLACK)


    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx * CELL_SIZE, r_idx*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,GRAY,one_rect,1)

    for one in bodies:
        b_rect = (one[0] * 40, one[1] * 40, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, b_rect)

    pygame.display.update()

pygame.quit()