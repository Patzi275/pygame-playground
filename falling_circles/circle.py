import pygame
import constantes

class Circle:
    def __init__(self, screen, radius, position, color):
        self.radius = radius
        self.position = position
        self.velocity = (0, 0)
        self.acceleration = (0, 0)
        self.color = color
        self.screen = screen

    
    def render(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)
    
    def getCenterPosition(self):
        return (self.position[0] + self.radius, self.position[1] + self.radius)
    
    def setCenterPosition(self, newPosition):
        self.position = (self.newPosition[0] - self.radius, self.newPosition[1] - self.radius)

    def physicUpdate(self):
        screenBottomLine = (0, self.screen.get_rect()[1] + self.screen.get_rect()[3])
        hVelocity = 0
        if self.isUnderLine(screenBottomLine):
            self.setOnLine(screenBottomLine)
            self.velocity = (self.velocity[0] + self.acceleration[0], -(self.velocity[1] + self.acceleration[1]) * constantes.BOUNCINGESS)
            pass
        else:
            self.acceleration = (self.acceleration[0] + constantes.WINDFORCE, self.acceleration[1] + constantes.GRAVITY)                
            self.velocity = (self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1])
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    # Fonction utilitaires
    def isUnderLine(self, _rect):
        return (self.position[1] + 2 * self.radius > _rect[1])
    
    def setOnLine(self, _rect):
        self.position = (self.position[0], _rect[1] - self.radius)


        
