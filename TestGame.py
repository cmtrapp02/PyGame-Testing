import pygame, sys
from pygame.locals import *

# used for setting the resolution of the window
class windowResolution:
    width = 600
    height = 400

# display the game window
def displayWindow():
    pygame.init()

    window_resolution = (600, 400)
    window = pygame.display.set_mode(window_resolution) # sets the size of the pygame screen
    pygame.display.set_caption('Test')

    return window

# draws the all surface objects
def drawSurfaceObjects(pos_x, pos_y):
    # gets the display window function
    window = displayWindow()

    # Colors
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    color_green = (0, 255, 0)
    color_blue = (0, 0, 255)

    window.fill(color_blue) # fills the entire surface with the chosen color
    rectangle = pygame.draw.rect(window, color_green, (pos_x, pos_y, 50, 50))


# main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pos_x = windowResolution.width / 2
        pos_y = windowResolution.height / 2
        surface = drawSurfaceObjects(pos_x, pos_y)

displayWindow()
main()
