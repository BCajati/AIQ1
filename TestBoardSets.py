from TileBoard3 import *
from copy import deepcopy

board1 = CreateInitialBoard()
board2 = deepcopy(board1)
board2.move_right()

frontierSet = {board1, board2}





#board2 = CreateChildBoard(board1)
#board2.move_right()

#frontierSet.add(board2)

for board in frontierSet:
    board.show()

