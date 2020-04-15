import pygame
import time

width, height = 400, 80
screen_size = (width, height)

pygame.init()
screen = pygame.display.set_mode(screen_size)

white = (225,225,225)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
bule = (0,0,255)
screen.fill(white)

green_rect = pygame.Rect((10,10),(30,30))
pygame.draw.rect(screen, green, green_rect)

red_rect = pygame.Rect((310,40),(80,30))
pygame.draw.rect(screen,red,red_rect)

pygame.display.flip()
time.sleep(10)

