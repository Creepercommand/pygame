import pygame
import time

black = (0, 0, 0)
white = (225, 225, 225)
red = (255, 0, 0)
green = (0, 225, 0)
blue = (0, 0, 225)

width, height = 400, 400
screen_size = (width, height)

pygame.init()
screen = pygame.display.set_mode(screen_size)
screen.fill(white)
# 블럭 그리기
block_size = 20

block_red = pygame.Rect((1 * block_size, 1 * block_size), (block_size, block_size))
pygame.draw.rect(screen, red, block_red)

block_green = pygame.Rect((1 * block_size, 3 * block_size), (block_size, block_size))
pygame.draw.rect(screen, green, block_green)

block_blue = pygame.Rect((1 * block_size, 5 * block_size), (block_size, block_size))
pygame.draw.rect(screen, blue, block_blue)

pygame.display.flip()
time.sleep(3)
