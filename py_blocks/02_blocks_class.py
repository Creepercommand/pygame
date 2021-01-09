import pygame

pygame.init()

SC_WIDTH, SC_HEIGHT = 600, 800
screen_size = (SC_WIDTH, SC_HEIGHT)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('py_blocks')

BLACK = (0,0,0)
YELLOW = (255, 255, 0)


class Block:
    def __init__(self, color, rect, speed=0):
        self.color = color
        self.rect = rect
        self.speed = speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


paddle = Block(YELLOW, pygame.Rect(300, 700, 100, 30))
ball = Block(YELLOW, pygame.Rect(300, 400, 20, 20), 10)
print("BALL : {}, PADDLE : {}".format(ball.speed, paddle.speed))
pygame.key.

running = True
# 게임 메인 루프
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle.rect.centerx -= 10
            if event.key == pygame.K_RIGHT:
                paddle.rect.centerx += 10

    screen.fill(BLACK)
    ball.draw()
    paddle.draw()
    pygame.display.update()

pygame.quit()
