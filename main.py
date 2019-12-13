
from game import *

test = game()

test.board = [
    [ 1, 2, 2 ],
    [ 1, 2, 1 ],
    [ 1, 1, 2 ]
]

print(test.check_win())
