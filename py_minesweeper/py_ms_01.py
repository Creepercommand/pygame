# py_mine_sweeper
#
# py_ms_01.py


# 01. 화면초기화
import pygame

# 파이게임 초기화
pygame.init()

# 변수 선언
COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
GRAY = (200, 200, 200)
BLACK = (0,0,0)

# 화면 생성
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('py_minesweeper')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # for y in range(ROW_COUNT):
    #     for x in range(COL_COUNT):
    #         one_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE,
    #                                CELL_SIZE,CELL_SIZE)
    #         pygame.draw.rect(screen,GRAY,one_rect,1)

    #선으로 분힐하기

    pygame.display.update()

# 파이게임 종료
pygame.quit()
