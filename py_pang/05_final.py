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

# 배경 설정
background_img = pygame.image.load(os.path.join(img_path, "background.png"))

# 무대 설정
stage_img = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_height = stage_img.get_rect().size[1]

# 캐릭터 설정
character_img = pygame.image.load(os.path.join(img_path, "character.png"))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height
character_speed = 0

# 무기 설정
weapon_img = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_width = weapon_img.get_rect().size[0]
weapon_speed = 10
weapons = []

# 공 설정
ball_img = [
    pygame.image.load(os.path.join(img_path, "balloon1.png")),
    pygame.image.load(os.path.join(img_path, "balloon2.png")),
    pygame.image.load(os.path.join(img_path, "balloon3.png")),
    pygame.image.load(os.path.join(img_path, "balloon4.png"))
]
ball_spd_y = [-18, -15. - 12, -9]
balls = [{
    'pos_x': 50,
    'pos_y': 50,
    'to_x': 3,
    'to_y': -6,
    'img_idx': 0,
    'init_spd_y': ball_spd_y[0]
}]

#제거할 공과 무기 인덱스 초기화
remove_ball_idx = -1
remove_weapon_idx = -1

# 게임 루프
running = True
while running:
    # FPS 처리
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
            elif event.key == pygame.K_SPACE:
                weapon_pos_x = character_x_pos + character_width // 2 - weapon_width // 2
                weapon_pos_y = character_y_pos
                weapons.append([weapon_pos_x, weapon_pos_y])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    # 캐릭터 움직임
    character_x_pos += character_speed

    # 벽 충돌
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 이동
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [[w[0], w[1]] for w in weapons if w[1] > -screen_height]

    # 캐릭터 영역 추출
    character_rect = character_img.get_rect()
    character_rect.top = character_y_pos
    character_rect.left = character_x_pos

    # 공 이동
    for cur_ball in balls:
        cur_ball_img = ball_img[cur_ball['img_idx']]
        cur_ball_rect = cur_ball_img.get_rect().size
        cur_ball_width = cur_ball_rect[0]
        cur_ball_height = cur_ball_rect[1]

        if cur_ball['pos_y'] > screen_height - stage_height - cur_ball_height:
            cur_ball['to_y'] = cur_ball['init_spd_y']
        else:
            cur_ball['to_y'] += 0.5
        if cur_ball['pos_x'] < 0 or cur_ball['pos_x'] > screen_width - cur_ball_width:
            cur_ball['to_x'] *= -1

        cur_ball['pos_x'] += cur_ball['to_x']
        cur_ball['pos_y'] += cur_ball['to_y']

    # 충돌 처리
    for idx_ball, one_ball in enumerate(balls):
        # 공 영역 추출
        one_ball_rect = ball_img[one_ball['img_idx']].get_rect()
        one_ball_rect.top = one_ball['pos_y']
        one_ball_rect.left = one_ball['pos_x']


        # 공과 캐릭터 충돌 확인
        if one_ball_rect.colliderect(character_rect):
            running = False
            print("GAME OVER")

    # 공과 무기 충돌 확인
        for idx_weapon, one_weapon in enumerate(weapons):
            one_weapon_rect = weapon_img.get_rect()
            one_weapon_rect.top = one_weapon[1]
            one_weapon_rect.left = one_weapon[0]
            if one_ball_rect.colliderect(one_weapon_rect):
                remove_ball_idx = idx_ball
                remove_weapon_idx = idx_weapon
                break
            if remove_weapon_idx > -1:
                del weapons[remove_weapon_idx]
                remove_weapon_idx = -1
            if remove_ball_idx > -1:
                del balls[remove_ball_idx]
                remove_ball_idx = -1

    # 화면 출력
    screen.blit(background_img, (0, 0))
    for one in weapons:
        screen.blit(weapon_img, (one[0], one[1]))
    for one in balls:
        screen.blit(ball_img[one['img_idx']], (one['pos_x'], one['pos_y']))
    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_x_pos, character_y_pos))

    # 화면 업데이트
    pygame.display.update()

# 파이게임 종료
pygame.quit()
