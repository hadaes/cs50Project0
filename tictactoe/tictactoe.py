"""
Tic Tac Toe Player
"""
import copy
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    if board == initial_state():
        return X
    if terminal(board):
        return None

    x_count = 0
    o_count = 0
    for row in board:
        for values in row:
            if values == X:
                x_count += 1
            elif values == O:
                o_count += 1
    if x_count > o_count:
        return O
    if o_count == x_count:
        return X
    else:
        raise Exception("O cannot outnumber X")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions_set = set()
    for y_values in range(3):
        for x_values in range(3):
            if board[x_values][y_values] == EMPTY:
                actions_set.add((x_values, y_values))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)

    i = action[0]
    j = action[1]

    if player(board) == X:
        item = X
    elif player(board) == O:
        item = O

    if board[i][j] != EMPTY:
        raise Exception("Space not empty")

    new_board[i][j] = item
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    x_win = False
    o_win = False

    center = board[1][1]

    # Check X diagonal
    if center == X:
        if center is board[1][1] and center is board[2][2]:
            return X
        elif center is board[2][0] and center is board[0][2]:
            return X

    # Check O diagonal
    elif center == O:
        if center is board[1][1] and center is board[2][2]:
            return O
        elif center is board[2][0] and center is board[0][2]:
            return O

    for row in board:
        if X in row and O not in row and EMPTY not in row:
            x_win = True
        if O in row and X not in row and EMPTY not in row:
            o_win = True

    for x_coord in range(3):
        if board[0][x_coord] == X:
            if board[1][x_coord] == X and board[2][x_coord] == X:
                x_win = True
        elif board[0][x_coord] == O:
            if board[1][x_coord] == O and board[2][x_coord] == O:
                o_win = True

    if x_win and o_win:
        raise Exception("Two winners not possible")
    if x_win:
        return X
    if o_win:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X or winner(board) == O:
        return True
    full = True
    for row in board:
        if EMPTY in row:
            full = False
    return full


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    # return a random action if computer makes first move
    if board == initial_state():
        action_list = []
        for move in actions(board):
            action_list.append(move)
        return action_list[random.randint(0, len(action_list)-1)]

    if player(board) == X:
        action_set = actions(board)
        result_set = []
        action_list = []
        for action in action_set:
            result_set.append(min_value(result(board, action)))
            action_list.append(action)
        thing = float("-inf")
        counter = 0
        index = 0
        for x in result_set:
            if x > thing:
                thing = x
                index = counter
            counter += 1
        return action_list[index]

    elif player(board) == O:
        action_set = actions(board)
        result_set = []
        action_list = []
        for action in action_set:
            result_set.append(max_value(result(board, action)))
            action_list.append(action)
        thing = float("inf")
        counter = 0
        index = 0
        for x in result_set:
            if x < thing:
                thing = x
                index = counter
            counter += 1
        return action_list[index]


def max_value(board):
    """
    Max value function
    """

    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    """
    Min value function
    """

    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
