
from game import *
from player_types import p

g = game()

g.game_loop(p.MAXIMIZING_PLAYER, p.MINIMIZING_PLAYER)

input()
