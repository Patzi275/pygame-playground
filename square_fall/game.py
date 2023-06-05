import pygame
from pygame.math import Vector2
import constantes
from barre import Barre
from circle_controller import CircleController
from square import Square, SquareType
from random import randint

class Game:
	clock = pygame.time.Clock()
	leftSpawningLimit = rightSpawningLimit = (0, 0)

	def __init__(self,screen):
    	#Initialisations and calcul
		self.screen = screen
		screenSize = screen.get_size()
		self.finalDest = (screenSize[0]/2, screenSize[1])
		pygame.time.set_timer(pygame.USEREVENT, constantes.SPAWNINGTIME)
		
		Game.leftSpawningLimit = (-screenSize[0] / 6 , -screenSize[1] / 6)
		Game.rightSpawningLimit = (screenSize[0] * 7 / 6 , Game.leftSpawningLimit[1])
	
		#Square 
		self.squareList = []

		#Barre
		self.barre = Barre(screen, 25, constantes.BLEUDARK)

		#CircleController
		middleBarrePositionn = (self.barre.rightPosition[0] - self.barre.leftPosition[0] / 2, self.barre.rightPosition[1])
		self.player = CircleController(self.screen, 15, middleBarrePositionn, constantes.BLANC)

	def start(self):
		self.squareList = []
		self.update()
	
	def update(self):
		loop = True
		while loop:
    		#Event
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.player.inverseMovingDirection()
				if event.type == pygame.QUIT:
					loop = False
				if event.type == pygame.USEREVENT:
					self.squareList.append(self.getNewSquare(30))

			#Update
			self.player.move()
			if self.checkForPlayerRedirection():
				self.player.inverseMovingDirection()

			#Render
			self.screen.fill(constantes.BLEUSOMBRE) #Clear screen
			self.barre.render()
			for sqr in self.squareList:
				sqr.update()
				sqr.render()
			self.player.render()
			
			pygame.display.flip()
			Game.clock.tick(60)
	
	def getNewSquare(self, dimension, speed = 3, _type = SquareType.MALUS):
		startDest = Game.getRandomPosition(Game.leftSpawningLimit, Game.rightSpawningLimit)
		direction = Vector2(Vector2(self.finalDest) - Vector2(startDest)).normalize()
		direction = (direction.x, direction.y)

		return Square(
			self.screen,
			pygame.Rect(startDest[0], startDest[1], dimension, dimension),
			_type, 
			speed, 
			direction)
	
	def checkForPlayerRedirection(self):
		if (self.player.position[0] < self.barre.leftPosition[0]):
			self.player.position = (self.barre.leftPosition[0], self.player.position[1])
			return True
		if (self.player.position[0] > self.barre.rightPosition[0]):
			self.player.position = (self.barre.rightPosition[0], self.player.position[1])
			return True

	def getRandomPosition(posA, posB):
		return (randint(posA[0], posB[0]), randint(posA[1], posB[1]))
	

class Game2:
	"""La classe permettant de gérer le jeu principal"""
	leftSpawningLimit = rightSpawningLimit = (0, 0)
	spawningTime = 28 * 2
	currentTime = 0

	def __init__(self, screen):
		self.screen = screen
		screenSize = screen.get_size()
		leftSpawningLimit = (-screenSize[0] / 6 , -screenSize[1] / 6)
		rightSpawningLimit = (screenSize[0] * 7 / 6 , leftSpawningLimit[1])
		

	def start(self):
		update()

	def update(self):
		loop = True
		while loop:
			currentTime += 1
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					loop = False
			

	def getRandomPosition(posA = leftSpawningLimit, posB = rightSpawningLimit):
		return (randint(leftSpawningLimit[0], rightSpawningLimit[0]),
				randint(leftSpawningLimit[1], rightSpawningLimit[1]))