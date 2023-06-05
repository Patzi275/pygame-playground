import pygame
from sprite2 import Sprite2
import constantes
import random

class Game:
    clock = pygame.time.Clock()
    def __init__(self, screen):
        self.screen = screen
        screensize = screen.get_rect()
        self.BRICKSIZE = (screensize[2] / 4, 25)
        self.spawningRects = []
        self.playerMovRects = []
        for i in range(4):
            tempRect = pygame.Rect(
                i * self.BRICKSIZE[0], 
                screensize[3], 
                self.BRICKSIZE[0], 
                self.BRICKSIZE[1])
            self.spawningRects.append(tempRect)

            tempRect = pygame.Rect(
                i * self.BRICKSIZE[0], 
                screensize[3] / 2, 
                self.BRICKSIZE[0], 
                self.BRICKSIZE[1]).center
            tempRect = pygame.Rect((tempRect[0] - 12, tempRect[1] - 12.5), (24, 25))
            self.playerMovRects.append(tempRect)
        

        #Bricks
        self.brick_group = pygame.sprite.Group()

        #Bol
        self.bolRadius = 18
        self.bol_group = pygame.sprite.Group()

        #Player
        self.playerMovingSens = 1
        self.player_group = pygame.sprite.Group()
        self.p1 = Sprite2(constantes.GREEN, self.playerMovRects[0], (4, 0))
        self.p2 = Sprite2(constantes.GREEN, self.playerMovRects[2], (4, 0))
        self.p1.add(self.player_group)
        self.p2.add(self.player_group)

        #Others
        self.score = 0
        self.nbLineBrick = 0
        self.font = pygame.font.Font("EASPORTS15.ttf", 60)
    
    def start(self):
        self.score = 0
        pygame.time.set_timer(pygame.USEREVENT, constantes.SPAWNINGTIME)
        self.brick_group.remove()
        self.bol_group.remove()
        self.update()

    def update(self):
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.playerMovingSens = -1
                    if event.key == pygame.K_RIGHT:
                        self.playerMovingSens = 1
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == pygame.USEREVENT:
                    self.generatBrickAndBol()

            self.removeIfOut(self.brick_group)
            self.removeIfOut(self.bol_group)

            if pygame.sprite.groupcollide(self.player_group, self.bol_group, False, True):
                self.score += 1
            if pygame.sprite.groupcollide(self.player_group, self.brick_group, False, False) != {}:
                break
            
            self.brick_group.update()
            self.bol_group.update()
            if self.playerMovChecker():
                self.player_group.update()
            
            self.screen.fill(constantes.BLUEDARK)
            self.drawScore(self.score)
            self.brick_group.draw(self.screen)
            self.bol_group.draw(self.screen)
            self.player_group.draw(self.screen)

            pygame.display.flip()
            Game.clock.tick(60)
    
    def generatBrickAndBol(self):
        choix = [False, False, False, False]
        if random.randint(0, 1) == 1:
            i = random.randrange(4)
            tempObj = Sprite2(constantes.WHITE, self.spawningRects[i], (0, constantes.MOVEUPSPEED))
            tempObj.add(self.brick_group)
            choix[i] = True
        else:
            i = random.randrange(2)
            tempObj = Sprite2(constantes.WHITE, self.spawningRects[i] , (0, constantes.MOVEUPSPEED))
            tempObj.add(self.brick_group)
            choix[i] = True
            tempObj = Sprite2(constantes.WHITE, self.spawningRects[i + 2], (0, constantes.MOVEUPSPEED))
            tempObj.add(self.brick_group)
            choix[i + 2] = True
            
        if self.nbLineBrick == 4:
            self.nbLineBrick = 0
            i = random.randrange(2)
            if i == 1:
                choix[choix.index(False)] = True
            _center = self.spawningRects[choix.index(False)].center
            _center = (_center[0] - self.bolRadius / 2,  _center[1] - self.bolRadius / 2)
            tempObj = Sprite2(constantes.GREEN, pygame.Rect(_center, (self.bolRadius, self.bolRadius)), (0, constantes.MOVEUPSPEED))
            tempObj.add(self.bol_group)
        
        self.nbLineBrick += 1

    def playerMovChecker(self):
        if self.playerMovingSens == 1:
            if self.p2.rect[0] < self.playerMovRects[3][0]:
                self.setPlayerVelocity(1)
                return True
            else:
                self.p2.rect = self.playerMovRects[3]
                self.p1.rect = self.playerMovRects[1]
                self.playerMovingSens = 0
                return False
        elif self.playerMovingSens == -1:
            if self.p1.rect[0] > self.playerMovRects[0][0]:
                self.setPlayerVelocity(-1)
                return True
            else:
                self.p1.rect = self.playerMovRects[0]
                self.p2.rect = self.playerMovRects[2]
                self.playerMovingSens = 0
                return False
        return False
                
    def setPlayerVelocity(self, sens):
        if sens == -1:
            for sp in self.player_group.sprites():
                sp.speed = (-abs(sp.speed[0]), 0)
        elif sens == 1:
            for sp in self.player_group.sprites():
                sp.speed = (abs(sp.speed[0]), 0)
    
    def drawScore(self, score):
        text = self.font.render(str(score), True, constantes.WHITE)
        textRect = text.get_rect()
        textRect.center = (self.screen.get_rect()[2] / 2, self.screen.get_rect()[3] / 6)
        self.screen.blit(text, textRect)

    def removeIfOut(self, theGroup):
        for sp in theGroup.sprites():
            rect = sp.image.get_rect()
            if rect[1] + rect[3] < 0:
                theGroup.remove(sp)
                del sp
    