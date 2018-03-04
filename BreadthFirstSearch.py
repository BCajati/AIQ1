from TileBoard3 import *
from copy import deepcopy
from queue import *

frontier = Queue()
explored = set()
visited = set()

def add_node_to_frontier(node):
    if node == None:
        return
    frontier.put(node)
    visited.add(node)

def breadth_first_search(board, goalBoard):
    nodes_expanded = 0
    finalBoard = None
    frontier.put(board)

    loop = 0
    visited.add(board)
    while True:
        loop += 1
        if frontier.empty():
            print("failure")
            break;

        node = frontier.get()
        nodes_expanded += 1
        explored.add(node)
        node.show()
        if boardsAreSame(node, goalBoard):
            print("Found Goal")
            finalBoard = node
          #  path_to_goal = node.node_path
            break;

        # add child nodes
        node1 = addMoveUpBoard(node)
        add_node_to_frontier(node1)
        node2 = addMoveRightBoard(node)
        add_node_to_frontier(node2)
        node3 = addMoveLeftBoard(node)
        add_node_to_frontier(node3)
        node4 = addMoveDownBoard(node)
        add_node_to_frontier(node4)
        if loop == 50:
            print("failure")
            break

    return finalBoard

