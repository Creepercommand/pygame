# 파이팡 최종본
# 2020.10.24

# 모듈 불러오기
import pygame
import os

# 파이게임 초기화
pygame.init()

# 화면 설정
screen_width = 680
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!!")

# 이미지 불러오기

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()
