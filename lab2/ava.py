import math

from exceptions import GameplayException
from connect4 import Connect4
from randomAgent import RandomAgent
from minMaxAgent import MinMaxAgent
import time

connect4 = Connect4()
agent1 = MinMaxAgent('o')
agent2 = MinMaxAgent('x')
wins = 0
looses = 0
draws = 0
i = 0
start = time.time()
searchDepth = 5
while i < 10:
    i += 1
    while not connect4.game_over:
        # connect4.draw()
        try:
            if connect4.who_moves == agent1.my_token:
                n_column = agent1.randomMove(connect4)
                # n_column = agent1.miniMax(connect4, True, searchDepth, 2, agent1.my_token)[0]
                # n_column = agent1.miniMaxPlus(connect4, True, searchDepth, 2, agent1.my_token)[0]
            else:
                # n_column = agent2.miniMax(connect4, True, searchDepth, 2, agent2.my_token)[0]
                # n_column = agent2.miniMaxPlus(connect4, True, searchDepth, 2, agent2.my_token)[0]
                n_column = agent2.miniMaxAB(connect4, True, searchDepth, 2, agent2.my_token, -math.inf, math.inf)[0]
            connect4.drop_token(n_column)
        except (ValueError, GameplayException):
            print('invalid move')
    if connect4.wins == 'x':
        wins += 1
    if connect4.wins == 'o':
        looses += 1
    if connect4.wins is None:
        draws += 1
    connect4 = Connect4()
# connect4.draw()
end = time.time()
print("search Depth: ", searchDepth)
print("time: ", end - start)
print("wins: ", wins)
print("looses: ", looses)
print("draws: ", draws)
