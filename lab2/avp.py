from exceptions import GameplayException
from connect4 import Connect4
from randomAgent import RandomAgent
import minMaxAgent


connect4 = Connect4()
agent = minMaxAgent.MinMaxAgent('x')
while not connect4.game_over:
    connect4.draw()
    try:
        if connect4.who_moves == agent.my_token:
            n_column = agent.miniMax(connect4, True, 3, 2, 'x')[0]
        else:
            n_column = int(input(':'))
        connect4.drop_token(n_column)
    except (ValueError, GameplayException):
        print('invalid move')

connect4.draw()
