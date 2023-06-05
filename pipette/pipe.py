import pygame

SCREENSIZE = (1366, 768)

def blitTextColor(screen):
    tColor = image.get_at([mousePosition[0], mousePosition[1]])
    
    text = font.render(str(tColor[:-1]), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (0, 0)

    textSurfaceRect = textRect.copy()
    textSurfaceRect.left += textSurfaceRect.width
    textSurfaceRect.width = textSurfaceRect.height 
    textSurface = pygame.Surface(textSurfaceRect.size)
    textSurface.fill(tColor)
    
    screen.blit(text, textRect)
    screen.blit(textSurface, textSurfaceRect)


lien = input("Entrez le lien vers l'image: ")

pygame.init()

image = pygame.image.load(lien)
imageSize = image.get_size()
if (imageSize[0] > SCREENSIZE[0] or imageSize[1] > SCREENSIZE[1]):
    imageSize = (imageSize[0] / 2, imageSize[1] / 2)
    image = pygame.transform.scale(image, imageSize)

screen = pygame.display.set_mode(imageSize)
pygame.display.set_caption("Picker")

image = image.convert_alpha()


font = pygame.font.Font("EASPORTS15.ttf", 32)

mousePosition = (0, 0)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEMOTION:
            mousePosition = event.pos
    
    screen.blit(image, (0, 0))
    
    blitTextColor(screen)

    pygame.display.flip()

pygame.quit()