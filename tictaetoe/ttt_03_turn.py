# ttt_03

# 보드 출력함수 prn_board(tb)
def prn_board(tb):
    for r in range(3):
        print("―" * 5)
        print("{}|{}│{}".format(tb[r][0], tb[r][1], tb[r][2]))


# 변수 초기화
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
turn = 'X'

# 보드 출력
prn_board(board)

# 9회동안 입력받기
for cnt in range(9):
    # 입력 좌표가 동일하면 재입력 받기
    while True:
        y, x = map(int, input('y, x: ').split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을수 없습니다. 다시 지정하세요.")
    # 좌표에 돌 놓기
    board[y][x] = turn
    prn_board(board)

    # 돌 모양 바꾸기
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'
