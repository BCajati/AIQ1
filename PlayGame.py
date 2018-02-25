from TileBoard3 import *
from copy import deepcopy
from queue import *

board1 = CreateInitialBoard()
board2 = deepcopy(board1)
board2.move_right()

frontier = Queue()
explored = {}
frontier.add(board1)

while frontier.empty() != True:
    node = frontier.pop()
    explored.add(node)
    # test which actions are possible and not already in explored or frontier



