#ttt_04_judge.py
#
# 틱텍토 판정

# 보드 출력 함수
def prn_board(tb):
    print("――――――――")
    print("   0 1 2")
    for i,line in enumerate(tb):
        print("  ――――――")
        print("{}||{}|{}│{}".format(i,line[0],line[1],line[2]))


# 변수 초기화
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


turn = 'X'

# 게임 루프(9회 반복)
prn_board(board)


for cnt in range(9):
    while True:
        # 좌표 입력 받기
        y, x = map(int, input('y, x: ').split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을 수 없습니다. 다시 지정하세요.")
    # 빈 칸이면 돌 놓은 후 보드 출력
    board[y][x] = turn
    prn_board(board)

    # 승리 판정
    if board[y][0] == board[y][1] == board[y][2] == turn:
        break
    if board[0][x] == board[1][x] == board[2][x] == turn:
        break

    # 턴 변경하기
    if turn == 'X':
        turn = 'O'
    elif turn == 'O':
        turn = 'X'

print("{} WIN!".format(turn))