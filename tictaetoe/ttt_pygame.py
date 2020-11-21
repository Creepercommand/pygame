import pygame

pygame.init()

screen_width = 450
screen_height = 450
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tic Tac Toe")

CELL_SIZE = 150
ROW_COUNT = screen_height // 3
COL_COUNT = screen_width // 3
WHITE = (225, 225, 225)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, WHITE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    pygame.display.update()

pygame.quit()
