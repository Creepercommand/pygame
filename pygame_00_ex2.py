# 1024 x 600 크기의 창 만들기
# 2020.04.11

import time, pygame

# 파이게임 초기화 및 생성하기
width, heigh = 1024, 600
win_size = (width,heigh)

# 창 만들기
screen = pygame.display.set_mode(win_size)
pygame.draw.rect(screen,(200,200,200), [10,10,10,50],2)
pygame.display.filp()
#창 유지하기
time.sleep(2)