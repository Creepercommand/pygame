# 파이팡 키 입력 처리
import pygame
import os

# 파이게임 초기화
pygame.init()
clock = pygame.time.Clock()

# 화면 설정
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("파이팡!")

# 이미지 경로 구하기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "image")

# 배경 이미지
background = pygame.image.load(os.path.join(img_path, "background.png"))

# 바닥 이미지
stage = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 케릭터 이미지
character = pygame.image.load(os.path.join(img_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height

# 무기
weapon = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

weapons = []

weapon_speed = 10

# 케릭터 이동속도
character_speed = 0

running = True
# 게임 루프
while running:
    FPS = 60
    clock.tick(FPS)
    # 파이게임 종료 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_speed = +5
            elif event.key == pygame.K_LEFT:
                character_speed = -5
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width // 2) - (weapon_width // 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    character_x_pos += character_speed
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    weapons = [[w[0], w[1]-weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 화면 그리기
    screen.blit(background, (0, 0))
    for one in weapons:
        screen.blit(weapon, one)

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 디스플레이 업데이트
    pygame.display.update()

pygame.quit()
