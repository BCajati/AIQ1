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

def boardFoundInSet(boardSet, board):
    for node in boardSet:
       if boardsAreSame(node, board):
            return True
    return False

board1 = CreateInitialBoard()
board2 = deepcopy(board1)
board2.move_right()
board3 = deepcopy(board1)
board3.move_down()

frontier = Queue()
frontier.put(board1)
frontier.put(board2)

visited = set()
visited.add(board1)
visited.add(board2)

#print(boardFoundInQueue(frontier, board1))
#print(boardFoundInQueue(frontier, board3))

print(boardFoundInSet(visited, board1))
print(boardFoundInSet(visited, board3))


#list1 = board1.sortedTiles()
#print(list1)

#print(boardsAreSame(board2, board2))
#print(boardsAreSame(board2, board3))
#print(board1.sortedTiles())
#print(board2.sortedTiles())



