import pygame
import os
import random

WHITE = (255, 255, 255)

SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("SPACE INVADER")
pygame.font.init()

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# 레이저
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))


BG = pygame.image.load(os.path.join("assets", "background-black.png"))
BG = pygame.transform.scale(BG, SCREEN_SIZE)

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x,self.y))

    def move(self,vel):
        self.y += vel

    def offscreen(self,height):
        return not(self.y <= height and self.y >=0)
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.ship_img = None
        self.health = health
        self.laser_img = None
        self.lasers = []

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def shoot(self):
        laser = Laser(self.x,self.y,self.laser_img)
        self.lasers.append(laser)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.max_health = health

    def move_lasers(self,vel):
        for laser in self.lasers:
            laser.move(vel)
            if laser.offscreen(SCREEN_HEIGHT):
                self.lasers.remove(laser)


class Enemy(Ship):
    COLOR_MAP = {
        "red": RED_SPACE_SHIP,
        "blue": BLUE_SPACE_SHIP,
        "green": GREEN_SPACE_SHIP
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img = self.COLOR_MAP[color]

    def move(self, vel):
        self.y += vel


def main():
    run = True
    player = Player(300, 650)
    player_vel = 5

    enemies = []
    wave_length = 5
    enemy_vel = 3

    laser_vel = 5

    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        Lives_lable = main_font.render(f"Lives: {lives}", 1, WHITE)
        Level_lable = main_font.render(f"Level: {level}", 1, WHITE)

        WIN.blit(Lives_lable, (10, 10))
        WIN.blit(Level_lable, (SCREEN_WIDTH - Level_lable.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if len(enemies) == 0:
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randint(50,700),
                              random.randint(-1000,-100),
                              random.choice(["red","blue","green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x < SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y < SCREEN_HEIGHT - player.get_height():
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in  enemies:
            enemy.move(enemy_vel)
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)
        player.move_lasers(-laser_vel)
main()
