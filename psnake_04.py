import pygame
import random

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PYSNAKE')
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 225)
GREEN = (0, 225, 0)
YELLOW = (225, 225, 0)

LEFT = 1
RIGHT = 3
UP = 5
DOWN = 2
direction = DOWN

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

center_pos = (COL_COUNT // 2, ROW_COUNT // 2)
bodies = [center_pos]

foods = []
for _ in range(10):
    while True:
        c_idx = random.randint(0, COL_COUNT - 1)
        r_idx = random.randint(0, ROW_COUNT - 1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        if event.key == pygame.K_RIGHT:
            direction = RIGHT
        if event.key == pygame.K_UP:
            direction = UP
        if event.key == pygame.K_DOWN:
            direction = DOWN

    head = bodies[0]
    c_idx = head[0]
    r_idx = head[1]
    if direction == LEFT:
        c_idx = c_idx - 1
    if direction == RIGHT:
        c_idx = c_idx + 1
    if direction == UP:
        r_idx = r_idx - 1
    if direction == DOWN:
        r_idx = r_idx + 1
    b_pos = (c_idx,r_idx)
    bodies.insert(0,b_pos)

    bodies.pop()


    screen.fill(BLACK)

    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx * CELL_SIZE, r_idx * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 1)

    for one in foods:
        f_rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                  CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, f_rect)

    for one in bodies:
        b_rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                  CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, b_rect)



    pygame.display.update()
    clock.tick(5)

pygame.quit()
