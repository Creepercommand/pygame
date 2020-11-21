import pygame

pygame.init()

screen_width = 450
screen_height = 450
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tae Toe")

WHITE = (225, 225, 225)
CELL_SIZE = 150
ROW_COUNT = screen_height // CELL_SIZE
COL_COUNT = screen_width // CELL_SIZE


# 격자 그리기 함수
def draw_grid():
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            rect = (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 3)


#  클릭한 셀의 좌표를 보드의 좌표로 변경
def cell_to_board(tm_pos):
    click_x = click_y = -1
    for y in range(3):
        if y * CELL_SIZE <= tm_pos[1] < (y + 1) * CELL_SIZE:
            click_y = y
    for x in range(3):
        if x * CELL_SIZE <= tm_pos[0] < (x + 1) * CELL_SIZE:
            click_x = x

    return click_x, click_y


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            if event.button == 1:
                click_x, click_y = cell_to_board(m_pos)
                print(click_x,click_y)

            if event.button == 3:
                running = False
    draw_grid()

    pygame.display.update()
pygame.quit()
