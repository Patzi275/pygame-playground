import pygame
import constantes

class Sprite2(pygame.sprite.Sprite):
    def __init__(self, color, r, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.rect = pygame.Rect(r[0], r[1], r[2], r[3])
        self.color = color
        self.image = pygame.surface.Surface((r[2], r[3]))
        if r[2] == r[3]:
            self.image.fill(constantes.BLUEDARK)
            pygame.draw.circle(self.image, color, (r[2] / 2, r[2] / 2), r[2] / 2)
        else:
            pygame.draw.rect(self.image, color, (0, 0, r[2], r[3]))
    
    def update(self):
        self.move()

    def move(self):
        self.rect = pygame.Rect((self.rect[0] + self.speed[0], self.rect[1] + self.speed[1]), (self.rect[2], self.rect[3]))