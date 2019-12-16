
from player_types import p


def minimax(game, player):
    '''perform minimax on the given board, as the given player (maximizing or minimizing)'''
    '''return a tuple of (score, position) where score was the score and position was the move that gave that score'''


    # if the current board state is the end of the game, return the score
    result = game.check_win()
    if result != None:
        # every return has a palceholder move with it
        if result == "tie": return [0, [0, 0]]
        if result == p.MINIMIZING_PLAYER: return [-1, [0, 0]]
        if result == p.MAXIMIZING_PLAYER: return [1, [0, 0]]


    # if we're the maximizing player
    if player == p.MAXIMIZING_PLAYER:

        # save the best score and best position for all our different options
        bestScore = -999999
        bestMove = [0, 0] # placeholder

        # loop over every coordinate position in the board
        for y in range(3):
            for x in range(3):

                # check if the position is empty
                if game.board[y][x] == p.EMPTY:

                    # move there (temporarily)
                    game.board[y][x] = player # player should be either p.MAXIMIZING_PLAYER or p.MINIMIZING_PLAYER

                    # check what its like to be here (by making he minimizing player make a move and seeing what they'd do)
                    score_for_this_position = minimax(game, p.MINIMIZING_PLAYER)[0] # [0] because the output is (score, position)

                    # if its better than the current best, remember it
                    if score_for_this_position >= bestScore:
                        bestScore = score_for_this_position
                        bestMove = [x, y]
                    
                    # move back to where we were
                    game.board[y][x] = p.EMPTY
                    
        # return what we found is the best move and position
        return [bestScore, bestMove]


    # if we're the minimizing player
    if player == p.MINIMIZING_PLAYER:

        # save the best score and best position for all our different options
        bestScore = 999999
        bestMove = [0, 0] # placeholder

        # loop over every coordinate position in the board
        for y in range(3):
            for x in range(3):

                # check if the position is empty
                if game.board[y][x] == p.EMPTY:

                    # move there (temporarily)
                    game.board[y][x] = player # player should be either p.MAXIMIZING_PLAYER or p.MINIMIZING_PLAYER

                    # check what its like to be here (by making he minimizing player make a move and seeing what they'd do)
                    score_for_this_position = minimax(game, p.MAXIMIZING_PLAYER)[0] # [0] because the output is (score, position)

                    # if its better than the current best, remember it
                    if score_for_this_position <= bestScore:
                        bestScore = score_for_this_position
                        bestMove = [x, y]
                    
                    # move back to where we were
                    game.board[y][x] = p.EMPTY
                    
        # return what we found is the best move and position
        return [bestScore, bestMove]
