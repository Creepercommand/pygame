import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PYSNAKE')
clock = pygame.time.Clock()

# 변수 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
BLUE = (0, 0, 225)
YELLOW = (255, 255, 0)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
STOP = 4
direction = DOWN

score = 0

score_font = pygame.font.SysFont("comicsans",40)


# 뱀
center = (COL_COUNT // 2, ROW_COUNT // 2)
bodies = [center]

def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT - 1)
        r_idx = random.randint(0, ROW_COUNT - 1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break

foods = []
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
            direction = RIGHT
        if event.key == pygame.K_UP:
            direction = UP
        if event.key == pygame.K_DOWN:
            direction = DOWN
        if event.key == pygame.K_SPACE:
            direction = STOP
        if event.key == pygame.K_s:
            score += 100


    head = bodies[0]
    c_idx = head[0]
    r_idx = head[1]
    if direction == LEFT:
        c_idx -= 1
    if direction == RIGHT:
        c_idx += 1
    if direction == UP:
        r_idx -= 1
    if direction == DOWN:
        r_idx += 1
    if direction == STOP:
        pass
    head_pos = (c_idx, r_idx)


    if head_pos in foods:
        foods.remove(head_pos)
        add_food()
        score += 10
        if direction is not STOP:
            bodies.insert(0, head_pos)
    else:
        if direction is not STOP:
            bodies.pop()
            bodies.insert(0, head_pos)

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

    score_img = score_font.render(f"Score:{score}",True,YELLOW)
    screen.blit(score_img,(10,10))

    pygame.display.update()
    clock.tick(10)




pygame.quit()
