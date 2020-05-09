import pygame
import random

WHITE = (225, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

player_url = 'd_images/player.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx=SCREEN_WIDTH // 2,
                                 bottom=SCREEN_HEIGHT)

enemy_url = 'd_images/wow.png'
enemy_img = pygame.image.load(enemy_url)
enemy_pos = enemy_img.get_rect(left=100, top=100)

enemies = list()
for cnt in range(3):
    enemy_pos = enemy_img.get_rect(left=700 * cnt + 100, top=100)
    enemies.append(enemy_pos)

pygame.key.set_repeat(1)

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 10
        elif event.key == pygame.K_RIGHT:
            player_pos.right += 10

    if player_pos.left < 0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    for one in enemies:
        one.top += 8
        if one.bottom > SCREEN_HEIGHT:
            one.top = -100
            one.left = random.randint(0, SCREEN_WIDTH - enemy_img.get_width() // 2)

    for one in enemies:
        screen.blit(enemy_img, one)

    screen.blit(player_img, player_pos)
    screen.blit(enemy_img, enemy_pos)
    clock.tick(144)
    pygame.display.flip()
