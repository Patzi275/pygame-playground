import pygame
import constantes
from enum import Enum

class SquareType(Enum):
    MALUS = 0
    BONUS = 1

class Square:
    def __init__(self, screen, rect, _type, speed, direction):
        self.screen = screen
        self.rect = rect
        self.type = _type
        if _type == SquareType.BONUS:
            self.color = constantes.BLANC
        else:
            self.color = constantes.BLEUAZURE
        self.velocity = (direction[0] * speed, direction[1] * speed)

        self.sprite = pygame.surface.Surface((rect[2], rect[3]))
        self.sprite.fill(self.color)

    def render(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        
        #Arranger rect pour ne pas perdre de temps
        self.screen.blit(self.sprite, (self.rect[0], self.rect[1]))

    
    def update(self):
        self.rect = (self.rect[0] + self.velocity[0], self.rect[1] + self.velocity[1], self.rect[2], self.rect[3])
    
