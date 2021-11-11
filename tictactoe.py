""" Tic Tac Toe Player """

import math
import copy

X = "X"
O = "O"
EMPTY = None
INFINITY = 9999


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
    if empty(board):
        return X
    elif isOturn(board):
        return O
    return X

def empty(board):
    for row in board:
        for tile in row:
            if tile!=EMPTY:
                return False
    return True

def full(board):
    for row in board:
        for tile in row:
            if tile==EMPTY:
                return False
    return True

def isOturn(board):
    cX= cO = 0
    for row in board:
        for tile in row:
            if tile == X:
                cX+=1
            elif tile == O:
                cO+=1
    return cX>cO
            
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    n =len(board)
    actions = set()
    for i in range(n):
        for j in range(n):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    tmpBoard = copy.deepcopy(board)
    tmpBoard[action[0]][action[1]] = p
    return tmpBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    n = len(board)
    rowWinner = colWinner = EMPTY
    rDiagonal = board[0][0]
    lDiagonal = board[2][0]
    for i in range(n):
        rowWinner = board[i][0]
        colWinner = board[0][i]
        
        for j in range(1,n):
            if rowWinner != EMPTY:
                if board[i][j] != rowWinner:
                    rowWinner = EMPTY
            if colWinner != EMPTY:
                if board[j][i] != colWinner:
                    colWinner = EMPTY           
            if i == j:
                if rDiagonal != EMPTY:
                    if board[i][j] != rDiagonal:
                        rDiagonal = EMPTY
                if lDiagonal != EMPTY:
                    if board[2-i][i] != lDiagonal:
                        lDiagonal = EMPTY
                    
        if rowWinner != EMPTY:
            return rowWinner#+"R"
        if colWinner != EMPTY:
            return colWinner#+"C"

    if rDiagonal != EMPTY:
        return rDiagonal#+"RD"
    if lDiagonal != EMPTY:
        return lDiagonal#+"LD"
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if full(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0

def optm(c1,c2,flag):
    c1opt = 1
    c2opt = 2
    if flag ==1:
        if(c1[0] > c2[0]):
            return c1opt
        elif (c2[0] > c1[0]):
            return c2opt
    elif flag ==0:
        if(c1[0] < c2[0]):
            return c1opt
        elif (c2[0] < c1[0]):
            return c2opt
    if c1[1] < c2[1]:
        return c1opt
    elif c2[1] < c1[1]:
        return c2opt
    else:
        return c1opt

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    action_s = list(actions(board))
    minimaxV = []
    p = player(board)
    print(p)
    if p == X:
        maxValue = (-INFINITY,INFINITY)
        rightAction = action_s[0]
        for action in action_s:
            resBoard = result(board,action)
            newValue = minmax(resBoard,0,O)
            if optm(maxValue,newValue,1)==2:
                maxValue= newValue
                rightAction = action
        optimalMove = rightAction
    else:
        minValue = (INFINITY,INFINITY)
        rightAction = action_s[0]
        for action in action_s:
            resBoard = result(board,action)
            newValue = minmax(resBoard,0,X)
            if optm(minValue,newValue,0)==2:
                minValue= newValue
                rightAction = action
        optimalMove = rightAction
    return optimalMove


def minmax(board,depth,player):
    if terminal(board):
        return (utility(board),depth)
    action_s = actions(board)
    if player == X:
        maxValue = (-INFINITY,INFINITY)
        for action in action_s:
            resBoard = result(board,action)
            newValue = minmax(resBoard,depth+1,O)
            if optm(maxValue, newValue,1) == 2:
                maxValue = newValue
        return maxValue
    else:
        minValue = (INFINITY,INFINITY)
        for action in action_s:
            resBoard = result(board,action)
            newValue = minmax(resBoard,depth+1,X)
            if optm(minValue, newValue,0) == 2:
                minValue = newValue
        return minValue

    
