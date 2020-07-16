"""
Test environment for tictactoe.py functions
"""

from tictactoe import *

X = "X"
O = "O"
EMPTY = None

board = [[O, X, EMPTY],
         [X, O, X],
         [EMPTY, X, O]]

print(winner(board))
