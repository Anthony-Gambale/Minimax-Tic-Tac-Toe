
# imports
from game import *
from player_types import *
import pygame as pyg
from math import floor
import time

# initialize pygame
pyg.init()

# some starting parameters
width = 400
height = width # for a square (making the screen a rectangle may cause things to be drawn out of place)
screen = pyg.display.set_mode((width, height))
white = (255, 255, 255)
yellow = (255, 218, 0)
red = (255, 0, 0)
text_color = red
screen.fill(white)
pyg.display.set_caption('TicTacToe (minimax)')

# init the game itself and some other tings
human = p.MAXIMIZING_PLAYER
ai = p.MINIMIZING_PLAYER


def text_objects(text, font):
    text_surf = font.render(text, 1, text_color)
    return text_surf, text_surf.get_rect()


def message_display(text):
    '''display a message to the screen'''
    large_text = pyg.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = (width/2, height/2)
    screen.blit(text_surf, text_rect)
    pyg.display.flip()
    time.sleep(2)


def get_mouse_click_move_coords():
    mouse_pos = pyg.mouse.get_pos()
    mouse_x, mouse_y = mouse_pos
    x = floor( (3*mouse_x)/width ) # coords of mouse click in terms of square
    y = floor( (3*mouse_y)/height )
    return x, y


def end_game(game):
    # draw the screen first - we want the text to be on top of their final screen
    game.draw_gui(screen, width, height)
    # draw the text
    result = game.check_win()
    if result == "tie": message_display("tie")
    else: message_display(convert[result] + " wins")
    game_loop()


def on_mouse_click(game):
    # move to that position
    x, y = get_mouse_click_move_coords()

    # check if the spot we clicked is open
    if game.board[y][x] == p.EMPTY:

        # move there
        game.board[y][x] = human

        # check for a winner
        game.draw_gui(screen, width, height)
        if game.refresh(): end_game(game)

        # have the ai move
        game.ai_move(ai)

        # check for a winner
        game.draw_gui(screen, width, height)
        if game.refresh(): end_game(game)


def game_loop():
    try:
        # some initialization stuff
        g = game()
        g.draw_gui(screen, width, height)

        while True:

            '''listen for events'''
            e = pyg.event.wait() # listen for events

            '''quit event'''
            if e.type == pyg.QUIT:
                raise StopIteration

            '''mouse click (of any type)'''
            if e.type == pyg.MOUSEBUTTONDOWN:
                on_mouse_click(g)
            
            '''make the changes i think'''
            pyg.display.flip()
        
    except StopIteration:
        # close the window
        pyg.quit()


# run the program
game_loop()
