import pygame
import random
import math

pygame.init()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


# 클래스 Block
class Block:
    def __init__(self, color, rect, speed=0):
        self.color = color
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45,45) +270

    # move 메서드
    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    # 그리기(draw) 메서드
    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            pygame.draw.ellipse(screen, self.color, self.rect)


# 화면 설정
SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)

screen = pygame.display.set_mode(SC_SIZE)
pygame.display.set_caption("PY_BLOCKS")

# 패들 볼
PADDLE = Block(YELLOW, pygame.Rect(300, 700, 300, 30))
BALL = Block(YELLOW, pygame.Rect(300, 400, 20, 20), 10)
BLOCKS = []

blocks_colors = [(255, 0, 0), (0, 250, 0), (0, 0, 250),
                 (223, 128, 255), (0, 255, 255), (255, 0, 255)]

for y_pos, bcolor in enumerate(blocks_colors):
    for x_pos in range(5):
        BLOCKS.append(Block(bcolor, pygame.Rect(x_pos * 100 + 60, y_pos * 50 + 40, 80, 30)))

# 키 반복 입력
pygame.key.set_repeat(5, 5)

# 폰트 설정
pyfont = pygame.font.SysFont(None, 80)
clear = pyfont.render('CLEAR!!', True, YELLOW)
game_over = pyfont.render('GAME OVER!!', True, YELLOW)

# 프레임
FPS = pygame.time.Clock()

# 게임 루프
running = True
while running:
    # 프레임 설정
    FPS.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and PADDLE.rect.centerx > 0:
                PADDLE.rect.centerx -= 5
            elif event.key == pygame.K_RIGHT and PADDLE.rect.centerx < SC_WIDTH:
                PADDLE.rect.centerx += 5

    # 공 이동하기
    if BALL.rect.centery < 1000:
        BALL.move()

    # 공과 벽 충돌
    if BALL.rect.centerx < 0 or BALL.rect.centerx > SC_WIDTH:
        BALL.dir = 180 - BALL.dir
    if BALL.rect.centery < 0:
        BALL.dir *= -1

    # 공과 패들 충돌
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80

    # 공과 벽돌 충돌
    pre_len = len(BLOCKS)
    BLOCKS = [one for one in BLOCKS if not one.rect.colliderect(BALL.rect)]
    if pre_len != len(BLOCKS):
        BALL.dir *= -1

    # 배경 색 칠하기
    screen.fill(BLACK)

    # 객체 그리기
    PADDLE.draw()
    BALL.draw()
    for one in BLOCKS:
        one.draw()

    #메시지 출력
    if BALL.rect.centery > SC_HEIGHT and len(BLOCKS) > 0:
        screen.blit(game_over,(SC_WIDTH // 2 - game_over.get_rect().width // 2, SC_HEIGHT//2))
    if len(BLOCKS) == 0:
        screen.blit(clear,(SC_WIDTH // 2 - clear.get_rect().width // 2, SC_HEIGHT//2))

   # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()
