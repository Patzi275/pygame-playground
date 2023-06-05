import pygame
from game import Game
import constantes

pygame.init()

window = pygame.display.set_mode((300, 600))
window.fill(constantes.WHITE)

jeu = Game(window)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            jeu.start()
    
    window.fill(constantes.WHITE)
    pygame.display.flip()
    
