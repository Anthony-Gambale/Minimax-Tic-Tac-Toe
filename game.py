
from player_types import *
from minimax import *

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
        board_is_full = p.EMPTY not in self.board[0] and p.EMPTY not in self.board[1] and p.EMPTY not in self.board[1]

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

    def draw(self):
        '''draw the contents of the board to the screen'''
        d = [ ['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        for y in range(3):
            for x in range(3):
                self.board[y][x] = convert[self.board[y][x]]
        for row in d:
            for column in row:
                print(column, end='')
            print()

    def refresh(self):
        '''draw the board and check if the game should be continued or not.'''
        self.draw()
        return self.check_win() != None # true if game is over, false if game is to be continued

    def game_loop(self, human, ai):
        '''loop through each players moves till the game is over'''
        '''human and ai will equal p.MINIMIZING_PLAYER or p.MAXIMIZING_PLAYER'''

        # if the game should be continued
        #while self.check_win() == None:
        while True:

            # separate the players move from the AI's move before them
            print()
            print("Your turn:")

            # refresh (break if our refreshing returns true)
            if self.refresh(): break

            # have the player move
            y = int(input("0, 1 or 2 for y: "))
            x = int(input("0, 1 or 2 for x: "))
            self.board[y][x] = human

            # refresh
            if self.refresh(): break

            # have the ai move
            move = minimax(self, ai)[1]
            self.board[move[1]][move[0]] = ai
        
        # after the loop, say who won
        if self.check_win() == "tie": print("tie")
        else:
            print(convert[self.check_win()])
