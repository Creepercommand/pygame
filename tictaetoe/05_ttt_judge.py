# 05_ttt_judge
#
# 대각선 판정


# 보드 출력 함수
def prn_board(tb):
    print("――――――――")
    print("   0 1 2")
    for i, line in enumerate(tb):
        print("  ――――――")
        print("{}||{}|{}│{}".format(i, line[0], line[1], line[2]))


#판정 함수
def judge(ty,tx):
    win = False
    if board[ty][0] == board[ty][1] == board[ty][2] == turn:
        win = True
    if board[0][tx] == board[1][tx] == board[2][tx] == turn:
        win = True
    if ty - tx == 0:
        if board[0][0] == board[1][1] == board[2][2] == turn:
            win = True
    if abs(ty - tx) == 2 or abs(ty - tx) == 0:
        if board[0][2] == board[1][1] == board[2][0] == turn:
            win = True
    return win

def change_stone(tt):
    if tt == 'X':
        return 'O'
    return 'X'

# 변수 초기화
msg = "비김"
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
turn = 'X'

# 게임 루프
prn_board(board)

for cnt in range(9):
    # 좌표 입력 받기
    while True:
        y, x = map(int, input("y, x: ").split(','))
        if board[y][x] == ' ':
            break
        print("돌을 놓을수 없습니다. 다시 지정하세요.")
    # 돌 놓기
    board[y][x] = turn
    prn_board(board)

    #판정
    if judge(y,x):
        msg = turn + "의 승리!!"
        break

    # 돌 모양 변경
    turn = change_stone(turn)

#결과
print(msg)
