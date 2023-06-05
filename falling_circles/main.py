import pygame
import random
from circle import Circle

def main():
    pygame.init()

    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 10)
    screen = pygame.display.set_mode((600, 600))

    circleList = []

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.USEREVENT:
                tempCircle = Circle(screen, random.randint(5, 30), (random.randint(1, 600), random.randint(1, 600)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255))
                circleList.append(tempCircle)
        screen.fill((0, 0, 0, 255))
        
        for circle in circleList:
            circle.physicUpdate()
            circle.render()
        
        pygame.display.flip()
        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()