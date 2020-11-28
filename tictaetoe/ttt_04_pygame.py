# 모듈 넣기
import pygame

# 파이게임 초기화
pygame.init()

# 변수 지정
screen_width = screen_height = 450
screen_size = (screen_width, screen_height)
cell_size = 150
row_count = screen_width // cell_size
col_count = screen_height // cell_size
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
turn = 'X'

TTTDATA = [[0 for _ in range(3)] for _ in range(3)]

# 돌 모양 설정
pygame.font.init()
result_font = pygame.font.SysFont('arial_black', 200)
turn_font = pygame.font.SysFont(' ', 110)
turn_x = turn_font.render('X', True, YELLOW)
turn_o = turn_font.render('O', True, YELLOW)
winner_x = turn_font.render('Winner X', True, WHITE)
winner_o = turn_font.render('Winner O', True, WHITE)

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Tic Tac Toe")


# 격자 그리기 함수
def draw_grid():
    for c in range(col_count):
        for r in range(row_count):
            rect = (c * cell_size, r * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect, 3)


# 변환 함수
def cell_to_board(tpos):
    for x in range(3):
        if cell_size * x < tpos[0] <= cell_size * x + cell_size:
            tcol = x

    for y in range(3):
        if cell_size * y < tpos[1] <= cell_size * y + cell_size:
            trow = y
    return tcol, trow


# 돌 모양 바꾸기
def change_turn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


def print_mark(p_row, p_col):
    turn_mark_rect = turn_o.get_rect().size
    p_x = p_col * cell_size + cell_size // 2 - turn_mark_rect[0] // 2
    p_y = p_row * cell_size + cell_size // 2 - turn_mark_rect[1] // 2
    if turn == 'X':
        screen.blit(turn_x, (p_x, p_y))
    else:
        screen.blit(turn_o, (p_x, p_y))


def check_winner(cw_row, cw_col):
    winner = False
    if TTTDATA[cw_row][0] == TTTDATA[cw_row][1] == TTTDATA[cw_row][2] == turn:
        winner = True
    if TTTDATA[0][cw_col] == TTTDATA[1][cw_col] == TTTDATA[2][cw_col] == turn:
        winner = True

    if cw_row - cw_col == 0:
        if TTTDATA[0][0] == TTTDATA[1][1] == TTTDATA[2][2] == turn:
            winner = True
    if cw_row - cw_col == 0 or abs(cw_row - cw_col) == 2:
        if TTTDATA[0][2] == TTTDATA[1][1] == TTTDATA[2][0] == turn:
            winner = True

    if winner:
        print_winner()

def reset_data():
    global turn
    global TTTDATA
    turn = 'X'
    TTTDATA = [[0 for _ in range(3)] for _ in range(3)]
    screen.fill(BLACK)
    pygame.display.update()



def print_winner():
    # pygame은 RGBA 를 지원하지 않는다.
    # layer(surface) 생성후 투명 이미지 출력

    result_surface = pygame.Surface((screen_width, screen_height))
    result_surface.set_alpha(200)
    result_surface.fill(BLACK)
    screen.blit(result_surface, (0, 0))

    global running
    win_rect = winner_o.get_rect(center=(screen_width // 2, screen_height // 2))
    if turn == 'O':
        screen.blit(winner_o, win_rect)
    else:
        screen.blit(winner_x, win_rect)
    pygame.display.update()
    pygame.time.delay(3000)
    reset_data()
    py_main()


# 메인 루프
running = True

def py_main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                col, row = cell_to_board(mouse_pos)
                if TTTDATA[row][col] == 0:
                    TTTDATA[row][col] = turn
                    # print(TTTDATA)
                    print_mark(row, col)
                    check_winner(row, col)
                    change_turn()

        # 격자 그리기
        draw_grid()

        pygame.display.update()
        # 메인 루프 종료

    pygame.quit()


py_main()