import pygame
def someFunc():
    window = pygame.display.set_mode((600, 400))
    color_red = (255, 0, 0)
    pos_x = 0
    pos_y = 0


    while True:
        pygame.draw.rect(window, color_red, (pos_x, pos_y, 50, 50))
        pos_x += .1
        pygame.display.update()

someFunc()
