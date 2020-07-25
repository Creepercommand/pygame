import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 변수 초기화
BLACK = (0, 0, 0)  # 배경색
GRAY = (128, 128, 128)  # 격자색
BLUE = (0, 0, 225)  # 뱀 색
GREEN = (0, 255, 0)  # 먹이색
YELLOW = (255, 255, 0)
RED = (255,0,0)
GAMEOVER = False
last_score = 0

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

LEFT, RIGHT, UP, DOWN, STOP = 0, 1, 2, 3, 4,
HACK = False
direction = STOP

score = 0

score_font = pygame.font.SysFont("comicsnas", 40)
gameover_font = pygame.font.SysFont("comicsnas", 80)

# 뱀 좌표 리스트
bodies = [(COL_COUNT // 2, ROW_COUNT // 2)]

foods = []


def add_food():
    while True:
        c_idx_ = random.randint(0, COL_COUNT - 1)
        r_idx_ = random.randint(0, ROW_COUNT - 1)
        f_pos = (c_idx_, r_idx_)
        if f_pos not in foods or f_pos not in bodies:
            foods.append(f_pos)
            break


for _ in range(10):
    add_food()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN and not GAMEOVER:
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
            HACK = True
        else:
            HACK = False

    screen.fill(BLACK)

    head = bodies[0]
    c_idx, r_idx = head[0], head[1]
    if direction == LEFT:
        c_idx -= 1
    elif direction == RIGHT:
        c_idx += 1
    elif direction == UP:
        r_idx -= 1
    elif direction == DOWN:
        r_idx += 1
    elif direction == STOP:
        pass
    head_pos = (c_idx, r_idx)
    if direction is not STOP and head_pos in bodies or c_idx < 0 or c_idx >= COL_COUNT or r_idx < 0 or r_idx >= ROW_COUNT:
        GAMEOVER = True
        direction = STOP
        last_score = score

    if HACK:
        bodies.insert(0, head_pos)
        # print(bodies)
        score += 10

    if head_pos in foods:
        foods.remove(head_pos)
        add_food()
        bodies.insert(0, head_pos)
        score += 10
    else:
        if not HACK and direction is not STOP:
            bodies.insert(0, head_pos)
            bodies.pop()

    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            rect = (c_idx * CELL_SIZE, r_idx * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

    for one in foods:
        rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

    for one in bodies:
        rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                CELL_SIZE, CELL_SIZE)
        if one == bodies[0]:
            pygame.draw.rect(screen, RED, rect)
        else:
            pygame.draw.rect(screen, BLUE, rect)


    score_img = score_font.render(f"SCORE:{score}", True, YELLOW)

    gameover_img = gameover_font.render("GAME OVER", True, YELLOW)
    lastscore_img = score_font.render(f"SCORE:{last_score}", True, YELLOW)
    screen.blit(score_img, (10, 10))
    if GAMEOVER:
        screen.blit(gameover_img, (SCREEN_WIDTH // 2 - gameover_img.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(lastscore_img, (SCREEN_WIDTH // 2 - lastscore_img.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(9)

pygame.quit()
