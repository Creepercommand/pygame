import pygame

WHITE = (225,225,225)
BLACK = (0,0,0)

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


player_url = 'd_images/player.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2,
                                 bottom = SCREEN_HEIGHT)
pygame.key.set_repeat(1)

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5
    if player_pos.left < 0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH


    screen.blit(player_img,player_pos)
    pygame.display.flip()
    clock.tick(144)
