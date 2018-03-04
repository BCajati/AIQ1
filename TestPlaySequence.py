from TileBoard3 import *
from copy import deepcopy
from queue import *
from time import perf_counter
from BreadthFirstSearch import *

#TODO - I think I am removing from queue while searching
#TODO - Need to add search in explored also

def doDebug():
    return False



def boardFoundInSet(boardSet, board):
    for node in boardSet:
       if boardsAreSame(node, board):
            return True
    return False




#def showFrontier():
#    while frontier.empty() != True:
#        board = frontier.get()
#        board.show()


#board1 = CreateStartBoard(2,1,0,3,4,5,6,7,8)

#works
#board1 = CreateStartBoard(3,1,2,0,4,5,6,7,8)

#works
#board1 = CreateStartBoard(3,1,2,6,4,5,0,7,8)

#works
#board1 = CreateStartBoard(3,1,2,6,4,5,7,0,8)

#doesn't work
#board1 = CreateStartBoard(4,1,2,3,0,5,6,7,8)

path_to_goal = []
cost_of_path = 0
nodes_expanded = 0
search_depth = 0
max_search_depth = 0


#board1 = CreateStartBoard(8,0,1,2,4,5,3,6,7)
board1 = CreateStartBoard(1,2,5,3,4,0,6,7,8)
board1.set_board_depth(0)

goalBoard = CreateGoalBoard()

perf_counter()
finalBoard = breadth_first_search(board1, goalBoard)


elapsed_time = perf_counter()

cost_of_path = finalBoard.get_board_depth
print( 'path_to_goal:' ,finalBoard.node_path)
print ('cost_of_path:', cost_of_path)
print('nodes_expanded:', nodes_expanded)
print('search_depth', finalBoard.get_board_depth())
print ('cost_of_path', cost_of_path)
print('elapsed_time', elapsed_time)
finalBoard.show()







