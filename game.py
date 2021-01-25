
from player_types import *
from minimax import *
from choice import choice
import pygame as pyg

def check3(a, b, c):
    '''check if 3 things are all equal'''
    return a == b and b == c


class game:
    '''This class will handle a single game of tictactoe.'''


    def __init__(self):
        '''init the board and the players'''

        # construct a board, where each cell is defined as empty
        self.board = [
            [ p.EMPTY, p.EMPTY, p.EMPTY ],
            [ p.EMPTY, p.EMPTY, p.EMPTY ],
            [ p.EMPTY, p.EMPTY, p.EMPTY ]
        ]


    def check_win(self):
        '''check if there is a winner, it is a tie, or the game should continue.'''

        # init winner
        winner = None

        # horizontal lines
        for row in self.board:
            if check3(row[0], row[1], row[2]) and row[0] != p.EMPTY:
                winner = row[0]
        
        # vertical lines
        for i in range(3):
            if check3(self.board[0][i], self.board[1][i], self.board[2][i]) and self.board[0][i] != p.EMPTY:
                winner = self.board[0][i]
        
        # diagonals
        if check3(self.board[0][0], self.board[1][1], self.board[2][2]) and self.board[0][0] != p.EMPTY:
            winner = self.board[0][0]
        if check3(self.board[0][2], self.board[1][1], self.board[2][0]) and self.board[0][2] != p.EMPTY:
            winner = self.board[0][2]
        
        # empty positions left?
        board_is_full = p.EMPTY not in self.board[0] and p.EMPTY not in self.board[1] and p.EMPTY not in self.board[2]

        # check
        if winner == None:
            if not board_is_full:
                return None
            else:
                return "tie"
        else:
            return winner
    

    def move(self, x, y, player):
        '''fill a position on the board, unless the game is over'''
        if self.check_win() != None:
            self.board[y][x] = player


    def draw_gui(self, screen, width, height):
        '''for drawing the game board to the screen'''
        '''b is the board (2D array of positions); s is the screen (pygame.display.set_mode thing)'''
        # set some variables
        b = self.board
        draw_color = (0, 0, 0)
        # fill the screen
        screen.fill((255, 255, 255))
        # draw the grid
        pyg.draw.line(screen, draw_color, (0, height/3), (width, height/3), 2)
        pyg.draw.line(screen, draw_color, (0, 2*height/3), (width, 2*height/3), 2)
        pyg.draw.line(screen, draw_color, (width/3, 0), (width/3, height), 2)
        pyg.draw.line(screen, draw_color, (2*width/3, 0), (2*width/3, height), 2)

        for y in range(3):
            for x in range(3):
                cell_x = round((x * width/3) + width/6)
                cell_y = round((y * height/3) + height/6)
                cell_pos = (cell_x, cell_y)
                # draw the circles
                if convert[b[y][x]] == "O":
                    pyg.draw.circle(screen, draw_color, cell_pos, round(width/9), 3) # relies on width and height being equal
                # draw the crosses
                if convert[b[y][x]] == "X":
                    buffer = width/(3*4) # width/(3*x) will be 1/x of a cell width
                    pyg.draw.line(screen, draw_color, (cell_x - buffer, cell_y - buffer), (cell_x + buffer, cell_y + buffer), 5)
                    pyg.draw.line(screen, draw_color, (cell_x - buffer, cell_y + buffer), (cell_x + buffer, cell_y - buffer), 5)


    def draw(self):
        '''draw the contents of the board to the screen'''
        print()
        print()
        d = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        for y in range(3):
            for x in range(3):
                d[y][x] = convert[self.board[y][x]]
        for row in d:
            for column in row:
                print(column, end='')
            print()


    def refresh(self):
        '''draw the board and check if the game should be continued or not.'''
        self.draw()
        return self.check_win() != None # true if game is over, false if game is to be continued


    def player_move_no_gui(self, player):
        y = choice("Please choose a row.", ["top", "middle", "bottom"]) # output is 0 1 or 2
        x = choice("Please choose a column.", ["left", "middle", "right"])
        while self.board[y][x] != p.EMPTY:
            print("That spot isn't empty.")
            y = choice("Please choose a row.", ["top", "middle", "bottom"]) # output is 0 1 or 2
            x = choice("Please choose a column.", ["left", "middle", "right"])
        self.board[y][x] = player


    def ai_move(self, player):
        move = minimax(self, player)[1]
        self.board[move[1]][move[0]] = player


    def game_loop_no_gui(self, human, ai):
        '''loop through each players moves till the game is over'''
        '''human and ai will equal p.MINIMIZING_PLAYER or p.MAXIMIZING_PLAYER'''

        # let the player go first if they wish
        if choice("Would you like to go first or second?", ["second", "first"]):
            self.refresh()
            y = choice("Please choose a row.", ["top", "middle", "bottom"]) # output is 0 1 or 2
            x = choice("Please choose a column.", ["left", "middle", "right"])
            while self.board[y][x] != p.EMPTY:
                print("That spot isn't empty.")
                y = choice("Please choose a row.", ["top", "middle", "bottom"]) # output is 0 1 or 2
                x = choice("Please choose a column.", ["left", "middle", "right"])
            self.board[y][x] = human

        # if the game should be continued
        #while self.check_win() == None:
        while True:

            # have the ai move
            self.ai_move(ai)

            # refresh
            if self.refresh(): break

            # have the player move
            self.player_move_no_gui(human)

            # refresh
            if self.refresh(): break
        
        # after the loop, say who won
        if self.check_win() == "tie": print("tie")
        else:
            print()
            print("result/winner: ", end='')
            print(convert[self.check_win()])
