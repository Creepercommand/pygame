import pygame

pygame.init()

screen_width = 450
screen_height = 450
CELL_SIZE = 150
WHITE = (225, 225, 225)
GRAY = (128, 128, 128)
ROW_COUNT = screen_height // CELL_SIZE
COL_COUNT = screen_width // CELL_SIZE
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tae Toe")

board = [[0 for _ in range(3)] for _ in range(3)]



# 격자 그리기 함수
def draw_grid():
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            rect = (y * CELL_SIZE, x * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 3)


# 셀 포인트를 행열로 변환 함수
def cell_to_board(tm_pos):
    row = col = -1
    for y in range(ROW_COUNT):
        if y * CELL_SIZE <= tm_pos[1] < (y + 1) * CELL_SIZE:
            row = y

    for x in range(COL_COUNT):
        if x * CELL_SIZE <= tm_pos[0] < (x + 1) * CELL_SIZE:
            col = x
    return row, col


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            if event.button == 1:
                r, c = cell_to_board(m_pos)
                #print("{}행 {}열".format(r, c))
                board[r][c] = 'X'
                print(board)

    draw_grid()
    pygame.display.update()

pygame.quit()
