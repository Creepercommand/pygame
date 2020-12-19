#recursive01

#재귀함수

def hello(cnt):
    if cnt == 0:
        return
    print('hello, recursive!')
    cnt = cnt - 1
    hello(cnt)



hello(3)