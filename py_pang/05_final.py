# 파이팡 최종본
# 2020.10.24

# 모듈 불러오기
import pygame
import os

# 파이게임 초기화
pygame.init()

# FPS
clock = pygame.time.Clock()

# 화면 설정
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!!")

# 이미지 불러오기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "image")

# 배경
background_img = pygame.image.load(os.path.join(img_path, "background.png"))

# 무대
stage_img = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_height = stage_img.get_rect().size[1]

# 캐릭터
character_img = pygame.image.load(os.path.join(img_path, "character.png"))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height
character_speed = 0

# 게임 루프
running = True
while running:
    #FPS 처리
    clock.tick(120)
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 종료 처리
            running = False
        # 키 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                character_speed = 5
            elif event.key == pygame.K_LEFT:
                character_speed = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    # 캐릭터 움직임
    character_x_pos += character_speed

    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width- character_width:
        character_x_pos = screen_width-character_width

    # 화면 출력
    screen.blit(background_img, (0, 0))
    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_x_pos, character_y_pos))

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()
