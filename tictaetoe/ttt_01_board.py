# ttt_01_board
# 보드 출력 함수 def prn_board(board)


def prn_board(board):
    for line in board:
        print("{}|{}│{}".format(line[0], line[1], line[2]))
        print("―" * 5)


board = [
    [' ', ' ', ''],
    [' ', ' ', ''],
    [' ', ' ', '']
]

prn_board(board)
