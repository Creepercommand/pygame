"""
『SPACE INVADER』
V1.1
"""
"""
★업데이트 노트★
__________________
V1.0 : 2020.06.27
게임 개발
__________________
2020.06.28
V1.1 업데이트
코드 촤적화
버그 수정
콘솔 정리 코드 추가
__________________
"""
# 모듈 불러오기
import pygame
import os
import random

# 변수 지정하기
WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화
pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("SPACE INVADER")

# 배경 이미지 불러오기
bg_img = pygame.image.load(os.path.join('assets', 'background-black.png'))
bg_img = pygame.transform.scale(bg_img, SCREEN_SIZE)

# 이미지 불러오기
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))
RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))

# 레이저 이미지 불러오기
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))
RED_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_red.png'))
BLUE_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_blue.png'))
GREEN_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_green.png'))


# 레이저 클래스 생성
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)  # 마스크 이미지 적용

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not (self.y <= height and self.y >= 0)

    # 접촉 감지
    def collision(self, obj):
        return collide(self, obj)


# 비행선 클래스
class Ship:
    COOLDOWN = 10  # 총알 발사 지연

    # ship 클래스 생성자
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.cool_down_counter = 0
        self.lasers = []
        self.laser_img = None

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    # 쿨다운 시스템
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # 레이저 움직이지
    def move_laser(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            # 레이저 삭제 여부 확인
            if laser.off_screen(SCREEN_HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


# 아군 클래스(ship 상속)
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.max_health = health
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)

    # 레이저 충돌확인
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(SCREEN_HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    # 충돌 확인
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.hbar(window)

    # 체력바 코드 (비행기 밑에 그려진다)- draw 커맨드로 같이 그림
    def hbar(self, window):
        # 빨간색 사각형
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10,
                          self.ship_img.get_width(), 10))
        # 초록색 사각형
        pygame.draw.rect(window, (0, 255, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10,
                          int(self.ship_img.get_width() * (self.health / self.max_health)), 10))


# 적군 클래스(ship 상속)
class Enemy(Ship):
    # 랜덤 색상 Dictionary
    COLOR_MAP = {
        'red': (RED_SPACE_SHIP, RED_LASER),
        'blue': (BLUE_SPACE_SHIP, BLUE_LASER),
        'green': (GREEN_SPACE_SHIP, GREEN_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    # 적 미사일 발사(ship 상속)
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


# 충돌 감지
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


# 메인 함수
def main():
    run = True  # 메인 루프(True, False)
    FPS = 120  # 초당 프레임

    level = 0  # 레벨
    lives = 5  # 생명

    main_font = pygame.font.SysFont("comicsans", 50)  # 폰트 설정

    player_vel = 5  # 플레이어 이동속도
    # Player(x,y,health)
    player = Player(300, 650)  # 플레이어 생성

    enemies = []  # 적군 처리 리스트
    wave_length = 5  # 한 레벨당 추가되는 적군수
    enemy_vel = 2  # 적군 속도

    laser_vel = 5  # 레이저 속도

    lost = False  # 게임 오버 여부 확인
    lost_count = 0  # 게임 오버후 시간 확인

    clock = pygame.time.Clock()

    # 화면 갱신
    def redraw_window():
        WIN.blit(bg_img, (0, 0))  # 배경

        lives_label = main_font.render(f"lives: {lives}", 1, WHITE)  # 생명 레이블
        level_label = main_font.render(f"level: {level}", 1, WHITE)  # 레벨 레이블

        # 레이블 그리기
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (SCREEN_WIDTH - level_label.get_width() - 10, 10))

        for enemy_ in enemies:  # 적군 그리기
            enemy_.draw(WIN)
        player.draw(WIN)  # 플레이어 그리기

        # 배경 업데이트
        pygame.display.update()

    # 게임 메인 루프
    while run:
        # 배경 업데이트
        redraw_window()
        clock.tick(FPS)

        # 게임 오버 여부 확인
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        # 3초 대기후 종료 코드
        if lost:
            if lost_count < FPS * 3:  # 3초 기다리는 코드
                run = False
            else:
                continue
        # 적군 만들기
        if len(enemies) == 0:
            wave_length += 5
            level += 1
            for i in range(wave_length):
                enemy = Enemy(random.randint(50, 650),
                              random.randint(-1000, -100),
                              random.choice(['red', 'green', 'blue']))
                enemies.append(enemy)
        # 창 끄기
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # 키 입력 받기
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel < SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel < SCREEN_HEIGHT - player.get_height():
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        # 적군 움직이기
        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_laser(laser_vel, player)

            # 레이저 발사
            if random.randint(0, 2 * FPS) == 1:
                enemy.shoot()

            # 플레이러 감지
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)

            # 바닥 감지
            if enemy.y + enemy.get_height() > SCREEN_HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        # 플리에어가 쏜 레이저 움직이기
        player.move_lasers(-laser_vel, enemies)


# 콘솔 정리
print("____________________")
print("   SPACE INVADER    ")
print("            V1.1    ")
print("____________________")
print("□□□□□□□□□□□□□□□□□□□□")
print("□□□□□□□□□■■□□□□□□□□□")
print("□□□□□□□□□■■□□□□□□□□□")
print("□□□□□□□□□■■□□□□□□□□□")
print("□□□□□□□■■■■■■□□□□□□□")
print("□□□□□□□■■■■■■□□□□□□□")
print("□□□□□□□■■■■■■□□□□□□□")
print("□□□□□□□■■■■■■□□□□□□□")
print("□□□■■■■■■■■■■■■■■□□□")
print("□□□■■■■■■■■■■■■■■□□□")
print("□□□□□□□□■■■■□□□□□□□□")
print("□□□□□□□□■■■■□□□□□□□□")
print("□□□□□□□□□□□□□□□□□□□□")

# 메인함수 실행
main()
