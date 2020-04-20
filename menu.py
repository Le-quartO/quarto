import sys, pygame
from pygame.locals import *
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1600, 900))

fond = pygame.image.load("image/menu.png").convert() # insere une image et la convertie au bon format"perso= pygame.image.load("perso.png").convert_alpha()

fenetre.blit(menu, (0,0))


