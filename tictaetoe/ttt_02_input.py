# 입력 받기


def prn_board(tb):
    for r in range(3):
        print("―" * 5)
        print("{}|{}│{}".format(tb[r][0], tb[r][1], tb[r][2]))



board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

prn_board(board)

for cnt in range(9):
    while True:
        y,x = map(int,input('y, x:').split(','))
        # y,x에 입력 가능한지 확인
        if board[y][x] == ' ':
            break
        print("돌을 놓을수 없습니다. 다시 지정하세요.")

    board[y][x] = "X"
    prn_board(board)
