from TileBoard3 import *
from copy import deepcopy
from queue import *

def listsAreSame(x, y, len):
    newList = [i for i, j in zip(x, y) if i == j]
    if newList.__len__() == len:
        return True
    else:
        return False

def boardsAreSame(board1, board2):
    if listsAreSame(board1.sortedTiles(), board2.sortedTiles(), 9):
        return True
    else:
        return False


def boardFoundInQueue(boardQueue, board):
    while boardQueue.empty() != True:
        if boardsAreSame(boardQueue.get(), board):
            return True
    return False

def addMoveDownBoard(node):
    if board1.can_move_down():
        nodeDown = deepcopy(node)
        nodeDown.move_down()
        # see if this board already exists in frontier
        if boardFoundInQueue(frontier, nodeDown) == False:
            print("Add Move Down")
            frontier.put(nodeDown)

def addMoveUpBoard(node):
    if board1.can_move_up():
        nodeUp = deepcopy(node)
        nodeUp.move_up()
        # see if this board already exists in frontier
        if boardFoundInQueue(frontier, nodeUp) == False:
            print("Add Move Up")
            frontier.put(nodeUp)

def addMoveRightBoard(node):
    if board1.can_move_right():
        nodeRight = deepcopy(node)
        nodeRight.move_right()
        # see if this board already exists in frontier
        if boardFoundInQueue(frontier, nodeRight) == False:
            print("Add Move Right")
            frontier.put(nodeRight)

def addMoveLeftBoard(node):
    if board1.can_move_left():
        nodeLeft = deepcopy(node)
        nodeLeft.move_left()
        # see if this board already exists in frontier
        if boardFoundInQueue(frontier, nodeLeft) == False:
            print("Add Move Left")
            frontier.put(nodeLeft)


def showFrontier():
    while frontier.empty() != True:
        board = frontier.get()
        board.show()


board1 = CreateInitialBoard()

frontier = LifoQueue()
explored = {}
frontier.put(board1)

addMoveRightBoard(board1)
addMoveLeftBoard(board1)
addMoveUpBoard(board1)
addMoveDownBoard(board1)




