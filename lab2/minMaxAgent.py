import copy
import math
import random
from exceptions import AgentException


class MinMaxAgent:

    def __init__(self, my_token='o'):
        self.my_token = my_token

    def goodMove(self, game, player):
        moves = game.possible_drops()
        result = 0
        if game.wins == player:
            result += 100
        if 2 not in moves:
            result += 10
        if game.wins != player and game.wins is not None:
            result -= 100
        return result

    def greatMove(self, game, player):
        moves = game.possible_drops()
        result = len(moves)
        if game.wins == player:
            result += 100
        if game.wins != player and game.wins != None:
            result -= 100
        for four in game.iter_fours():
            if four == [player, player, player, '_']:
                result += 20
            if four == ['_', player, player, player]:
                result += 20
            if four == [player, '_', player, player]:
                result += 10
            if four == [player, player, '_', player]:
                result += 10
            if four == ['_', player, player, '_']:
                result += 5
            if four == [player, player, '_', '_']:
                result += 5
            if four == ['_', '_', player, player]:
                result += 5

        return result

    def randomMove(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')
        return random.choice(connect4.possible_drops())

    def miniMax(self, game, isMaximizing, depth, lastMove, player):
        if game.game_over or depth == 0:
            currentScore = self.goodMove(game, player)
            return (lastMove, currentScore)
        if isMaximizing:
            bestScore = -math.inf
        else:
            bestScore = math.inf
        bestMove = -1
        for move in game.possible_drops():
            neighbor = copy.deepcopy(game)
            neighbor.drop_token(move)
            bestNeighbor = self.miniMax(neighbor, not isMaximizing, depth - 1, move, player)
            # randomize move
            if bestNeighbor[1] == bestScore:
                decision = random.random() > 0.5
                if decision:
                    bestScore = bestNeighbor[1]
                    bestMove = move
            if (bestNeighbor[1] > bestScore and isMaximizing) or (bestNeighbor[1] < bestScore and not isMaximizing):
                bestScore = bestNeighbor[1]
                bestMove = move
        return (bestMove, bestScore)

    def miniMaxPlus(self, game, isMaximizing, depth, lastMove, player):
        if game.game_over or depth == 0:
            currentScore = self.greatMove(game, player)
            return (lastMove, currentScore)
        if isMaximizing:
            bestScore = -math.inf
        else:
            bestScore = math.inf
        bestMove = -1
        for move in game.possible_drops():
            neighbor = copy.deepcopy(game)
            neighbor.drop_token(move)
            bestNeighbor = self.miniMaxPlus(neighbor, not isMaximizing, depth - 1, move, player)
            # randomize move
            if bestNeighbor[1] == bestScore:
                decision = random.random() > 0.5
                if decision:
                    bestScore = bestNeighbor[1]
                    bestMove = move
            if (bestNeighbor[1] > bestScore and isMaximizing) or (bestNeighbor[1] < bestScore and not isMaximizing):
                bestScore = bestNeighbor[1]
                bestMove = move
        return (bestMove, bestScore)

    def miniMaxAB(self, game, isMaximizing, depth, lastMove, player, a, b):
        if game.game_over or depth == 0:
            currentScore = self.greatMove(game, player)
            return (lastMove, currentScore)
        if isMaximizing:
            bestScore = -math.inf
        else:
            bestScore = math.inf
        bestMove = -1
        for move in game.possible_drops():
            neighbor = copy.deepcopy(game)
            neighbor.drop_token(move)
            bestNeighbor = self.miniMaxAB(neighbor, not isMaximizing, depth - 1, move, player, a, b)
            if (bestNeighbor[1] > bestScore and isMaximizing) or (bestNeighbor[1] < bestScore and not isMaximizing):
                bestScore = bestNeighbor[1]
                bestMove = move
                if bestScore >= a:
                    a = bestScore
                if bestScore <= b:
                    b = bestScore
            if a <= b:
                break
        return (bestMove, bestScore)



