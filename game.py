
from enum import Enum

def check3(a, b, c):
    '''check if 3 things are all equal'''
    return a == b and b == c


class p(Enum):
    '''Enumerate all the states for positions on the board'''
    EMPTY = 0
    MAXIMIZING_PLAYER = 1
    MINIMIZING_PLAYER = 2


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
