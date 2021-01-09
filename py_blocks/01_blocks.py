import pygame

pygame.init()

SC_WIDTH, SC_HEIGHT = 600,800
screen_size = (SC_WIDTH,SC_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('py_blocks')

running = True
# 게임 메인 루프
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False