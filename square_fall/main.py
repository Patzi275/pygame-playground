import pygame
import constantes
from game import Game

def main():
	pygame.init()

	screen = pygame.display.set_mode((360, 600))

	myGame = Game(screen)

	loop = True
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				myGame.start()
			if event.type == pygame.QUIT:
				loop = False
				
		screen.fill((100, 100, 100, 255))
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()