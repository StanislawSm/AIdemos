import math
import random

from exceptions import AgentException
class MinMaxOut:

    def __init__(self, my_token='o'):
        self.my_token = my_token

    def make_best_move(self, connect4):
        bestScore = -math.inf
        bestMove = None
        gameCopy = connect4.copy()
        for move in gameCopy.get_possible_moves():
            gameCopy.make_move(move)
            score = minimax(False, aiPlayer, ticTacBoard)
            ticTacBoard.undo()
            if (score > bestScore):
                bestScore = score
                bestMove = move
        ticTacBoard.make_move(bestMove)

    def minimax(isMaxTurn, maximizerMark, board):
        state = board.get_state()
        if (state is State.DRAW):
            return 0
        elif (state is State.OVER):
            return 1 if board.get_winner() is maximizerMark else -1

        scores = []
        for move in board.get_possible_moves():
            board.make_move(move)
            scores.append(minimax(not isMaxTurn, maximizerMark, board))
            board.undo()

        return max(scores) if isMaxTurn else min(scores)