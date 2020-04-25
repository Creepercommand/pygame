import pygame
import ctypes
from pygame.locals import *

WHITE = (225,225,225)
BLACK = (0,0,0)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

player_url = 'd_images/player.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect()

player_pos.left = SCREEN_WIDTH //2 - player_img.get_width()
player_pos.top = SCREEN_HEIGHT - player_img.get_height()

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == ord('f'):  # f 키를 눌렀을 때
                user32 = ctypes.windll.user32
                screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)  # 해상도 구하기
                surface = pygame.display.set_mode(screensize, FULLSCREEN)  # 전체화면으로 전환

    screen.blit(player_img, player_pos)

    pygame.display.flip()