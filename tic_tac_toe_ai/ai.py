import math

target = 'o'

def evaluate(game):
    win = game.check_win()
    if win:
        return 10 if game.XO != target else -10
    return 0

def minmax(game, depth, isMax):
    score = evaluate(game)
    if score == 10 or score == -10:
        return score

    if game.draw:
        return 0
    
    if isMax:
        best = -math.inf
        for i in range(1, 4):
            for j in range(1, 4):
                if game.canPlay(i, j):
                    game.play(i, j)
                    best = max(best, minmax(game, depth + 1, not isMax))
                    game.undo()
        return best
    else:
        best = math.inf
        for i in range(1, 4):
            for j in range(1, 4):
                if game.canPlay(i, j):
                    game.play(i, j)
                    best = min(best, minmax(game, depth + 1, not isMax))
                    game.undo()
        return best

def findBestMove(game):
    bestVal = -math.inf
    bestMove = (None, None)

    for i in range(1, 4):
        for j in range(1, 4):
            if game.canPlay(i, j):
                game.play(i, j)
                val = minmax(game, 0, False)
                game.undo()
                if val > bestVal:
                    bestVal = val
                    bestMove = (i, j)
    return bestMove



