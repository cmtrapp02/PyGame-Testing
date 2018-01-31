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
    pygame.display.update()
