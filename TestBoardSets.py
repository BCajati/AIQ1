from TileBoard3 import *
from copy import deepcopy


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


def boardFound(boardSet, board):
    return True

board1 = CreateInitialBoard()
board2 = deepcopy(board1)
board2.move_right()

#list1 = board1.sortedTiles()
#print(list1)

print(boardsAreSame(board2, board2))

#print(board1.sortedTiles())
#print(board2.sortedTiles())



