import pygame as pg
import sys
import time
from random import choice
from pygame.locals import *
from game import Game
import ai

game = Game()

width = 400
height = 400

white = (255, 255, 255)
black = (0, 0, 0)
line_color = (0, 0, 0)

pg.init()
fps = 30
CLOCK = pg.time.Clock()

screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("tic tac toe".title())

initiating_window = pg.image.load("images/back.png")
x_img = pg.image.load("images/x.png")
o_img = pg.image.load("images/o.png")

initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))


def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    #updating the display
    pg.display.update()
    time.sleep(1)
    screen.fill(white)

    #drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    #drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
    # getting the global variable draw
    global game

    if game.winner is None:
        message = game.XO.upper() + "'s Turn"
    else:
        message = game.winner.upper() + " won !"
    if game.draw:
        message = "Game Draw !"

    # setting a font properties like
    font = pg.font.Font(None, 30)

    text = font.render(message, 1, white)
    screen.fill(black, (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global game
    # checking for winnig row
    win_line = game.check_win()
    if win_line:
        sens = win_line[0]
        num = row = col = int(win_line[1])
        if sens == 'r':
            pg.draw.line(screen, 
                (250, 0, 0),
                (0, (row + 1)*height / 3 - height / 6),
                (width, (row + 1)*height / 3 - height / 6),
                4)
        elif sens == 'c':
            pg.draw.line(screen, 
                (250, 0, 0),
                ((col + 1)*width / 3 - width / 6, 0),
                ((col + 1)*width / 3 - width / 6, height),
                4)
        elif sens == 'd':
            if num == 0:
                pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
            elif num == 1:
                pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    draw_status()

def drawXO(row, col):
    global game

    if row == 1:
        posx = 30
    elif row == 2:
        posx = width / 3 + 30
    elif row == 3:
        posx = width / 3 * 2 + 30
    
    if col == 1:
        posy = 30
    elif col == 2:
        posy = height / 3 + 30
    elif col == 3:
        posy = height / 3 * 2 + 30

    if (game.XO == 'x'):
        screen.blit(x_img, (posy, posx))
    else:
        screen.blit(o_img, (posy, posx))

    pg.display.update()

def getClickedCase():
    x, y = pg.mouse.get_pos()
    if (x < width/3):
        col = 1
    elif (x < width/3*2):
        col = 2
    elif (x < width):
        col = 3
    else:
        col = None

    if (y < height/3):
        row = 1
    elif (y < height/3*2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None
    
    return (row, col)

def on_user_click():
    global game
    row, col = getClickedCase()

    if (game.canPlay(row, col)):
        drawXO(row, col)
        game.play(row, col)
        check_win()

def ai_play():
    global game
    row, col = ai.findBestMove(game)
    if not (row and col):
        while True:
            row = choice([1, 2, 3])
            col = choice([1, 2, 3])
            if game.canPlay(row, col):
                break
        print(f"RAND ({row}, {col})")
    else:
        print(f"IA   ({row}, {col})")

    
    drawXO(row, col)
    game.play(row, col)
    check_win()

def reset_game():
    global game
    game.reset(choice(['x', 'o']))    
    game_initiating_window()

game_initiating_window()

while(True):
    user_clicked = False
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_clicked = True
            
    if game.XO == 'x' and user_clicked:
        on_user_click()
    elif game.XO == 'o':
        ai_play()
        #game.XO = 'x'

    if (game.isFinished()):
        time.sleep(3)
        reset_game()
        
    pg.display.update()
    CLOCK.tick(fps)
