import pygame
import random
import time


WHITE = (225,255,225)
BLACK = (0,0,0)
YELLOW = (0,150,0)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

enemy_num =4
score = 0

gameover = False

#파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Dead GAME^^ - Creeper_coding")
frame = pygame.time.Clock()
pygame.key.set_repeat(1)

pygame.mixer.init()
bgm_url = 'd_images/Tony Iggy - Astronomia.mid'
pygame.mixer.music.load(bgm_url)
pygame.mixer.music.play(-1)

small_font = pygame.font.SysFont("Agency FB",36)
large_font = pygame.font.SysFont("HYNAML",72)

player_url = "d_images/player.png"
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2,
                                 bottom = SCREEN_HEIGHT)

enemy_url = "d_images/wow.png"
enemy_img = pygame.image.load(enemy_url)
enemies_info = []
for cnt in range(enemy_num):
    enemy_pos = enemy_img.get_rect(left = random.randint(0,SCREEN_WIDTH- enemy_img.get_width()),
                                   bottom = -200 * cnt)
    enemy_speed = random.randint(3,10)
    enemies_info.append([enemy_pos,enemy_speed])

while True:
    screen.fill(WHITE)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos.left -= 8
            if event.key == pygame.K_RIGHT:
                player_pos.left += 8

    if player_pos.left < 0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    if not gameover:
        for one in enemies_info:
            one[0].top +=one[1]
            if one[0].top > 800:
                one[0].left = random.randint(0,SCREEN_WIDTH - enemy_img.get_width())
                one[0].top = -100
                one[1] = random.randint(3,8)
                score += 1


    screen.blit(player_img,player_pos)
    for one in enemies_info:
        screen.blit(enemy_img,one[0])
        if one[0].colliderect(player_pos):
            gameover = True


    #점수 출력
    score_img = small_font.render("SCORE: {}".format(score), True,YELLOW)
    screen.blit(score_img,(10,10))

    if gameover:
        gameover_img = large_font.render("게임종료",True, YELLOW)
        screen.blit(gameover_img, (SCREEN_WIDTH // 2 -gameover_img.get_width() // 2,
                                   SCREEN_HEIGHT // 2 -gameover_img.get_height() // 2))
    frame.tick(144)
    pygame.display.flip()

