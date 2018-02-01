import pygame, sys
from pygame.locals import *

pygame.init()
window_width = 400
window_height = 300
window = pygame.display.set_mode((1600, 1300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Blue = pygame.Color(0, 0, 255)
    pygame.display.update()
    pygame.Surface.set_at((0, 0), Blue)
