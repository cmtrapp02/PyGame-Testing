import pygame, sys
from pygame.locals import *

pygame.init()

# display window
def display_window():
    window_width = 1600
    window_height = 1300
    window = pygame.display.set_mode((window_width, window_height), 0,32)
    pygame.display.set_caption('Test')

    return window

#rectangles
def rectangles():

    # set up colors
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    color_green = (0, 255, 0)
    color_blue = (0, 0, 255)

    # draw rectangles to screen
    screen = display_window()
    screen.fill(color_white)
    pygame.draw.line(screen, color_red, (120, 60), (0, 0), 5)


# main game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


# execution
display_window()
rectangles()
game_loop()
