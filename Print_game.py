import pygame, sys, os
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500, 500))

player = pygame.image.load(os.path.join("print_0.jpeg"))
player.convert()

while True:
    screen.blit(player, (10, 10))
    pygame.display.flip()

pygame.quit()
