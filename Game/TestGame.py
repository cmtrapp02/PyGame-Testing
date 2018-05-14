import pygame, sys
from pygame.locals import *

# display the game window
def displayWindow():
    pygame.init()

    width = 600
    height = 400
    window = pygame.display.set_mode((width, height)) # sets the size of the pygame screen
    time = pygame.time.Clock()

    return window, width, height

# draws the all surface objects
def drawSurfaceObjects(pos_x, pos_y):
    # gets the display window function
    window, _, _ = displayWindow()

    # Colors
    color_black = (0, 0, 0)
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    color_green = (0, 255, 0)
    color_blue = (0, 0, 255)

    window.fill(color_black) # fills the entire surface with the chosen color
    pygame.draw.rect(window, color_white, (pos_x, pos_y, 10, 10)) # draws a rectangle that will be the player

# main game loop
def main():

    _, width, height = displayWindow()
    pos_x = width / 2
    pos_y = height / 2
    key = pygame.key.get_pressed()
    #timer = pygame.time.set_timer()
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() 
                sys.exit()
       
        #TODO switch from fixed timestep to variable timestep
        #limits the framerate to 15 frames per second
        pygame.time.Clock()
       
        print(pygame.time.Clock().get_time())
       
        # Gets the player surface object and its xy coordinates for input
        surface = drawSurfaceObjects(pos_x, pos_y)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            pos_x += .5
        if key[pygame.K_s]:
            pos_y += .5
        if key[pygame.K_a]:
            pos_x += -.5
        if key[pygame.K_w]:
            pos_y += -.5
        
        
        pygame.display.update()

        

displayWindow()
#drawSurfaceObjects()
main()
