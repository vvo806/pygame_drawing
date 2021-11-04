# imports
import pygame, sys
from pygame.locals import *

# initalize pygame
pygame.init()

# assign FPS(frame per second)
FPS = 30
clock = pygame.time.Clock()

#setup colors
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# display dimensions
width = 300
height = 300
# setup a 300x300 pixel display
displaysurf = pygame.display.set_mode((width, height))
displaysurf.fill(WHITE)
pygame.display.set_caption("my drawing")

# create lines and shapes
pygame.draw.line(displaysurf, BLUE, (150, 130), (130, 170)) #coordinate points (starting point), (ending point)
pygame.draw.line(displaysurf, BLUE, (150, 130), (170, 170))
pygame.draw.line(displaysurf, GREEN, (130, 170), (170, 170))
pygame.draw.circle(displaysurf, BLACK, (100,50), 30)

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() #quits the game
            sys.exit()

    # refreshing display/screen
    pygame.display.update()
    clock.tick(FPS)
