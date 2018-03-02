from TileBoard3 import *
from copy import deepcopy
from queue import *

#TODO - I think I am removing from queue while searching
#TODO - Need to add search in explored also

def doDebug():
    return False

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

def boardFoundInSet(boardSet, board):
    for node in boardSet:
       if boardsAreSame(node, board):
            return True
    return False

def addMoveDownBoard(node):
    if node.can_move_down():
        if doDebug():
            node.show()
        nodeDown = deepcopy(node)
        nodeDown.move_down()
        # see if this board already exists in frontier
        if boardFoundInSet(visited, nodeDown) == False:
            print("Add Move Down")
            frontier.put(nodeDown)
            visited.add(nodeDown)

def addMoveUpBoard(node):
    if node.can_move_up():
        if doDebug():
            board1.show()
        nodeUp = deepcopy(node)
        nodeUp.move_up()
        # see if this board already exists in frontier
        if boardFoundInSet(visited, nodeUp) == False:
            #print("Add Move Up")
            frontier.put(nodeUp)
            visited.add(nodeUp)

def addMoveRightBoard(node):
    if node.can_move_right():
        nodeRight = deepcopy(node)
        nodeRight.move_right()
        # see if this board already exists in frontier
        if boardFoundInSet(visited, nodeRight) == False:
            #print("Add Move Right")
            frontier.put(nodeRight)
            visited.add(nodeRight)

def addMoveLeftBoard(node):
    if node.can_move_left():
        nodeLeft = deepcopy(node)
        nodeLeft.move_left()
        # see if this board already exists in frontier
        if boardFoundInSet(visited, nodeLeft) == False:
            print("Add Move Left")
            frontier.put(nodeLeft)
            visited.add(nodeLeft)


def showFrontier():
    while frontier.empty() != True:
        board = frontier.get()
        board.show()


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

goalBoard = CreateGoalBoard()

frontier = Queue()
explored = set()
visited = set()
frontier.put(board1)

loop = 0
visited.add(board1)
while True:
    loop += 1
    if frontier.empty():
        print("failure")
        break;

    node = frontier.get()
    #path_to_goal.append(",")
    path_to_goal.append(node.get_board_move())
    nodes_expanded += 1
    explored.add(node)
    node.show()
    if boardsAreSame(node, goalBoard):
        print("Found Goal")
        path_to_goal = node.node_path
        break;

    # add child nodes
    addMoveUpBoard(node)
    addMoveRightBoard(node)
    addMoveLeftBoard(node)
    addMoveDownBoard(node)
    if loop == 50:
        print("failure")
        break


print( 'path_to_goal:' ,path_to_goal)
print ('cost_of_path:', cost_of_path)
print('nodes_expanded:', nodes_expanded)
print('search_depth', search_depth)







