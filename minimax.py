
class p(Enum):
    '''Enumerate all the states for positions on the board'''
    EMPTY = 0
    MAXIMIZING_PLAYER = 1
    MINIMIZING_PLAYER = 2

def minimax(board, player):
    '''perform minimax on the given board, as the given player (maximizing or minimizing)'''
    '''return a tuple of (score, position) where score was the score and position was the move that gave that score'''


    # if we're the maximizing player
    if player == p.MAXIMIZING_PLAYER:

        # save the best score and best position for all our different options
        bestScore = -999999
        bestMove = [0, 0] # placeholder

        # loop over every coordinate position in the board
        for y in range(3):
            for x in range(3):

                # check if the position is empty
                if board[y][x] == p.EMPTY:

                    # move there (temporarily)
                    board[y][x] = player # player should be either p.MAXIMIZING_PLAYER or p.MINIMIZING_PLAYER

                    # check what its like to be here (by making he minimizing player make a move and seeing what they'd do)
                    score_for_this_position = minimax(board, p.MINIMIZING_PLAYER)[0] # [0] because the output is (score, position)

                    # if its better than the current best, remember it
                    if score_for_this_position > bestScore:
                        bestScore = score_for_this_position
                        bestMove = [x, y]
                    
        # return what we found is the best move and position
        return [bestScore, bestMove]


    # if we're the minimizing player
    if player == p.MAXIMIZING_PLAYER:

        # save the best score and best position for all our different options
        bestScore = -999999
        bestMove = [0, 0] # placeholder

        # loop over every coordinate position in the board
        for y in range(3):
            for x in range(3):

                # check if the position is empty
                if board[y][x] == p.EMPTY:

                    # move there (temporarily)
                    board[y][x] = player # player should be either p.MAXIMIZING_PLAYER or p.MINIMIZING_PLAYER

                    # check what its like to be here (by making he minimizing player make a move and seeing what they'd do)
                    score_for_this_position = minimax(board, p.MINIMIZING_PLAYER)[0] # [0] because the output is (score, position)

                    # if its better than the current best, remember it
                    if score_for_this_position > bestScore:
                        bestScore = score_for_this_position
                        bestMove = [x, y]
                    
        # return what we found is the best move and position
        return [bestScore, bestMove]