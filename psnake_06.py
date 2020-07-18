import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
GRAY = (128,128,128)
BLUE = (0,0,255)
YEllOW = (255,255,0)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

LEFT = 0
RIGHt = 1
UP = 2
DOWN = 3
STOP =4
HACK = 5
direction = DOWN

score = 0
score_font = pygame.font.SysFont("comicsans", 40)

center = (COL_COUNT // 2 ,ROW_COUNT // 2)
bodies = []
foods = []
def add_food():
    while True:
        c_idx = random.randint(0,COL_COUNT - 1)
        r_idx = random.randint(0,ROW_COUNT -1)
        f_pos = (c_idx,r_idx)
        if f_pos is not bodies or f_pos is not foods:
            foods.append(f_pos)
            break

for _ in range(10):
    add_food()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        if event.key == pygame.K_RIGHT:
            direction = RIGHt
        if event.key == pygame.K_UP:
            direction = UP
        if event.key == pygame.K_DOWN:
            direction = DOWN
        if event.key == pygame.K_SPACE:
            direction = STOP
        if event.key == pygame.K_s:
            direction = HACK

