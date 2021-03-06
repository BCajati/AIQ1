from copy import deepcopy

def doDebug():
    return False

class Tile(object):
    #Tried using row/col but sorting too hard in python
    #Instead use index as 0..9 position index

    def __init__(self, index, value):
        self.index = index
        self.value = value
        self.numColumns = 3

    def move_left(self):
        self.index = self.index - 1

    def move_right(self):
        self.index = self.index + 1

    def move_up(self):
        self.index = self.index - self.numColumns

    def move_down(self):
        self.index = self.index + self.numColumns

    def is_empty_tile(self):
        return True if self.value == 0 else False

    def show(self):
        print("index: ", self.index, "val: ", self.value)

class TileBoard(object):

    def __init__(self, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9):

        self.depth = 0
        self.numColumns = 3
        self.board_move = ""
        self.node_path = ""
        self.tileList = []
        self.tileList.append(tile1)
        self.tileList.append(tile2)
        self.tileList.append(tile3)
        self.tileList.append(tile4)
        self.tileList.append(tile5)
        self.tileList.append(tile6)
        self.tileList.append(tile7)
        self.tileList.append(tile8)
        self.tileList.append(tile9)
        for x in self.tileList:
            if x.value == 0:
                self.tile_zero = x

    def set_board_mode(self, move):
        self.board_move = move

    def get_board_move(self):
        return self.board_move

    def set_board_depth(self, boardDepth):
        self.depth = boardDepth

    def get_board_depth(self):
        return self.depth

    def set_node_path(self, parent_path):
        self.node_path = parent_path + ',' +  self.board_move

    def get_node_path(self):
        return self.node_path

    def tiles(self):
        return self.tileList

    def sortedTiles(self):
        tileValues = []
        sortedList = sorted(self.tileList, key=indexSort)
        tileValues.append(sortedList[0].value)
        tileValues.append(sortedList[1].value)
        tileValues.append(sortedList[2].value)
        tileValues.append(sortedList[3].value)
        tileValues.append(sortedList[4].value)
        tileValues.append(sortedList[5].value)
        tileValues.append(sortedList[6].value)
        tileValues.append(sortedList[7].value)
        tileValues.append(sortedList[8].value)
        return tileValues

    def can_move_up(self):
        if self.tile_zero.index in (3,4,5,6,7,8):
            return True
        else:
           return False

    def can_move_down(self):
        if self.tile_zero.index in (0,1,2,3,4,5):
            return True
        else:
            return False

    def can_move_left(self):
        if self.tile_zero.index in (1,2,4,5,7,8):
            return True
        else:
            return False

    def can_move_right(self):
        if self.tile_zero.index in (0, 1, 3, 4, 6, 7):
            return True
        else:
            return False

    def move_left(self):
        tileIndexToSwap = self.tile_zero.index - 1
        tileToSwap = self.find_tile(tileIndexToSwap)
        self.tile_zero.move_left()
        tileToSwap.move_right()
        self.board_move = "Left"
        self.node_path += ", Left"

    def move_right(self):
        tileIndexToSwap = self.tile_zero.index + 1
        tileToSwap = self.find_tile(tileIndexToSwap)
        self.tile_zero.move_right()
        tileToSwap.move_left()
        self.board_move = "Right"
        self.node_path += ",Right"


    def move_up(self):
        tileIndexToSwap = self.tile_zero.index - self.numColumns
        tileToSwap = self.find_tile(tileIndexToSwap)
        self.tile_zero.move_up()
        tileToSwap.move_down()
        self.board_move = "Up"
        self.node_path += ",Up"


    def move_down(self):
        tileIndexToSwap = self.tile_zero.index + self.numColumns
        tileToSwap = self.find_tile(tileIndexToSwap)
        self.tile_zero.move_down()
        tileToSwap.move_up()
        self.board_move = "Down"
        self.node_path += ",Down"

    def find_tile(self, atIndex):
        for tile in self.tileList:
            if tile.index == atIndex:
                return tile

    def show(self):
        sortedList = sorted(self.tileList, key=indexSort)
        print(sortedList[0].value, ",", sortedList[1].value, ",", sortedList[2].value )
        print(sortedList[3].value, ",", sortedList[4].value, ",", sortedList[5].value)
        print(sortedList[6].value, ",", sortedList[7].value, ",", sortedList[8].value, "\n")

def addMoveDownBoard(node):
    if node.can_move_down():
        if doDebug():
            node.show()
        nodeDown = deepcopy(node)
        nodeDown.move_down()
        nodeDown.set_board_depth(node.get_board_depth() + 1)
        # see if this board already exists in frontier
        return nodeDown
    else:
        return None

def addMoveUpBoard(node):
    if node.can_move_up():
        if doDebug():
            node.show()
        nodeUp = deepcopy(node)
        nodeUp.move_up()
        nodeUp.set_board_depth(node.get_board_depth() + 1)
        return nodeUp
    else:
        return None


def addMoveRightBoard(node):
    if node.can_move_right():
        nodeRight = deepcopy(node)
        nodeRight.move_right()
        nodeRight.set_board_depth(node.get_board_depth() + 1)
        return nodeRight
    else:
        return None

def addMoveLeftBoard(node):
    if node.can_move_left():
        nodeLeft = deepcopy(node)
        nodeLeft.move_left()
        nodeLeft.set_board_depth(node.get_board_depth() + 1)
        return nodeLeft
    else:
        return None

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

def indexSort(Tile):
    return Tile.index

def CreateChildBoard(existingBoard):
    childList = sorted(existingBoard.tiles, key=indexSort)
    return TileBoard(childList[0], childList[1], childList[2], childList[3], childList[4], childList[5],
                     childList[6], childList[7], childList[8])


def CreateInitialBoard1():
    tile1 = Tile(0,0)
    tile2 = Tile(1,9)
    tile3 = Tile(2,5)
    tile4 = Tile(3,1)
    tile5 = Tile(4,8)
    tile6 = Tile(5,2)
    tile7 = Tile(6,3)
    tile8 = Tile(7,4)
    tile9 = Tile(8,6)
    return TileBoard(tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9)


def CreateInitialBoard():
    tile1 = Tile(0,1)
    tile2 = Tile(1,0)
    tile3 = Tile(2,2)
    tile4 = Tile(3,3)
    tile5 = Tile(4,4)
    tile6 = Tile(5,5)
    tile7 = Tile(6,6)
    tile8 = Tile(7,7)
    tile9 = Tile(8,8)
    return TileBoard(tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9)


def CreateStartBoard(value1, value2, value3, value4, value5, value6, value7, value8, value9):
    tile1 = Tile(0, value1)
    tile2 = Tile(1, value2)
    tile3 = Tile(2, value3)
    tile4 = Tile(3, value4)
    tile5 = Tile(4, value5)
    tile6 = Tile(5, value6)
    tile7 = Tile(6, value7)
    tile8 = Tile(7, value8)
    tile9 = Tile(8, value9)
    return TileBoard(tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9)

def CreateGoalBoard():
    tile1 = Tile(0,0)
    tile2 = Tile(1,1)
    tile3 = Tile(2,2)
    tile4 = Tile(3,3)
    tile5 = Tile(4,4)
    tile6 = Tile(5,5)
    tile7 = Tile(6,6)
    tile8 = Tile(7,7)
    tile9 = Tile(8,8)
    return TileBoard(tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9)

