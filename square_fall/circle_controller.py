import pygame

class CircleController:
    def __init__(self, scene, radius, position, color, speed = 2):
        self.scene = scene
        self.radius = radius
        self.color = color
        self.position = position
        self.speed = speed
    
    def render(self):
        pygame.draw.circle(self.scene, self.color, self.position, self.radius)
    
    def move(self):
        self.position = (self.position[0] + self.speed, self.position[1])
    
    def inverseMovingDirection(self):
        self.speed *= -1