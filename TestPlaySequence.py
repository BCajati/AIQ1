from TileBoard3 import *
from copy import deepcopy
from queue import *

def listsAreSame(x,y, len):
    newList = [i for i, j in zip(x,y) if i == j]
    if newList.__len__() == len:
        return True
    else:
        return False

def boardsAreSame(board1, board2):
    if listsAreSame(board1.sortedTileList, board2.sortedTileList):
        return True
    else:
        return False

def boardFound(boardSet, board):
    return True

board1 = CreateInitialBoard()

frontier = Queue()
explored = {}
frontier.add(board1)


# test which actions are possible
if board1.can_move_down():
    nodeDown = deepcopy(board1)
    nodeDown.move_down()
    # see if this board already exists in frontier