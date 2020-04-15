import pygame
import time

WHITE = (225,225,225)
BLACK = (0,0,0)
RED =(225,0,0)
GREEN = (0,225,0)
BLUE = (0,0,225)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLOCK_SIZE = 20

def draw_block(screen, color, position):
    x_position = position[0]
    y_position = position[1]
    block = pygame.Rect((x_position*BLOCK_SIZE, y_position*BLOCK_SIZE) ,(BLOCK_SIZE,BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)




screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

#블럭 그리기
draw_block(screen, RED,(1,1))
draw_block(screen, RED,(1,3))
draw_block(screen, RED,(1,5))
draw_block(screen, RED,(1,7))
draw_block(screen, GREEN,(3,1))
draw_block(screen, GREEN,(3,3))
draw_block(screen, GREEN,(3,5))
draw_block(screen, GREEN,(3,7))
draw_block(screen, BLUE,(5,1))
draw_block(screen, BLUE,(5,3))
draw_block(screen, BLUE,(5,5))
draw_block(screen, BLUE,(5,7))

pygame.display.flip()
pygame.init()
time.sleep(3)