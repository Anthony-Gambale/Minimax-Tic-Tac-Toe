
from enum import Enum

class p(Enum):
    '''Enumerate all the states for positions on the board'''
    MINIMIZING_PLAYER = -1
    EMPTY = 0
    MAXIMIZING_PLAYER = 1

convert = {
    p.MAXIMIZING_PLAYER: 'X',
    p.MINIMIZING_PLAYER: 'O',
    p.EMPTY: '-'
}
