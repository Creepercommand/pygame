# space03
# 2020.05-23

import os
import pygame
import random

WHITE = (255, 255, 255)

# 화면 설정
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("SPACE INVADER")
pygame.font.init()

#레이저 이미지 불러오기
RED_LAZER = pygame.image.load(os.path.join('assets','pixel_laser_red.png'))
BLUE_LAZER = pygame.image.load(os.path.join('assets','pixel_laser_blue.png'))
GREEN_LAZER = pygame.image.load(os.path.join('assets','pixel_laser_green.png'))
YELLOW_LAZER = pygame.image.load(os.path.join('assets','pixel_laser_yellow.png'))
#적군 이미지 불러오기
RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))

BG_IMG = pygame.image.load(os.path.join('assets', 'background-black.png'))
BG_IMG = pygame.transform.scale(BG_IMG, SCREEN_SIZE)


# Ship 비행선 클래스 생성
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.lazer_img = None

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.max_health = health
        self.mask = pygame.mask.from_surface(self.ship_img)


class Enemy(Ship):
    COLOR_MAP = {
        'red': (RED_SPACE_SHIP, RED_LAZER),
        'blue': (BLUE_SPACE_SHIP, BLUE_LAZER),
        'green': (GREEN_SPACE_SHIP,GREEN_LAZER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.lazer_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicasans", 50)
    lost_font = pygame.font.SysFont("comicasans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    player = Player(300, 650)

    lost_count = 0
    lost = False

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG_IMG, (0, 0))

        lives_lable = main_font.render(f"Lives {lives}", 1, WHITE)
        level_lable = main_font.render(f"Level {level}", 1, WHITE)
        WIN.blit(lives_lable, (10, 10))
        WIN.blit(level_lable, (SCREEN_WIDTH - level_lable.get_width() - 10, 10))

        player.draw(WIN)

        for enemy in enemies:
            enemy.draw(WIN)

        if lost:
            lost_lable = lost_font.render('YOU LOST!!', 1, WHITE)
            WIN.blit(lost_lable,
                     ((SCREEN_WIDTH - lost_lable.get_width()) / 2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        # 기회가 없거나 채력이 없으면 3초간 대기
        if lives < 1 or player.health < 1:
            lost_count += 1
            lost = True

        if lost:
            if lost_count > FPS * 3:
                run = False

            else:
                continue

        # 파이게임 종료 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # 아군 비행선 키 입력 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= player_vel
        if keys[pygame.K_w] and player.y > 0:
            player.y -= player_vel
        if keys[pygame.K_d] and player.x < SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_s] and player.y < SCREEN_HEIGHT - player.get_height():
            player.y += player_vel

        # 적군 비행선 초기화(비행선 목록이 빈 경우에만 실행)
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randint(50, SCREEN_WIDTH - 100),
                              random.randint(-1500, -100),
                              random.choice(['red', 'blue', 'green']))  # 0은 색상값
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y > SCREEN_HEIGHT:
                lives -= 1
                enemies.remove(enemy)


main()
