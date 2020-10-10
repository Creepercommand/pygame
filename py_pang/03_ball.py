import pygame
import os

# 파이게임 초기화
pygame.init()

# 화면 생성
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!")

# 배경이미지
cu_path = os.path.dirname(__file__)
img_path = os.path.join(cu_path,"image")
bg = pygame.image.load(os.path.join(img_path, "background.png"))

#바닥 이미지
stage = pygame.image.load(os.path.join(img_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#케릭터 이미지
character = pygame.image.load(os.path.join(img_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width //2 - character_width //2
character_y_pos = screen_height - stage_height -character_height


# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0,0))
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))
    pygame.display.update()

# 게임종료
pygame.quit()
