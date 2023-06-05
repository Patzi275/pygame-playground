import pygame

class Barre:
    def __init__(self, screen, height, color, leftPosition = (0, 0), rightPosition = (0, 0)):
        self.leftPosition = leftPosition
        self.rightPosition = rightPosition
        self.color = color
        self.height = height
        self.radius = height / 2
        self.screen = screen


        screenSize = screen.get_size()
        if (self.leftPosition == (0, 0)):
            self.leftPosition = (screenSize[0] * 2.5 / 10 - self.radius, screenSize[1] / 2 - self.radius)
        if (self.rightPosition == (0, 0)):
            self.rightPosition = (screenSize[0] * 8 / 10 - self.radius, screenSize[1] / 2 - self.radius)
        
        print(self.__dict__)
        
    def render(self):
        pygame.draw.circle(self.screen, self.color, self.leftPosition, self.radius)
        pygame.draw.circle(self.screen, self.color, self.rightPosition, self.radius)
        _rect = pygame.rect.Rect(
            self.leftPosition[0] - self.radius / 4,
            self.leftPosition[1] - self.radius, 
            self.rightPosition[0] - self.leftPosition[0] + 5, 
            self.height - 1
        )
        pygame.draw.rect(self.screen, self.color, _rect)
