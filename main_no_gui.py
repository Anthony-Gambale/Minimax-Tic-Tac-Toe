
from game import *
from player_types import p

while True:

    g = game()
    g.game_loop_no_gui(p.MAXIMIZING_PLAYER, p.MINIMIZING_PLAYER)
    input("press any key to continue...")
