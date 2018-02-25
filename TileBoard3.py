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
        self.row = self.index + self.numColumns

    def is_empty_tile(self):
        return True if self.value == 0 else False

    def show(self):
        print("index: ", self.index, "val: ", self.value)

class TileBoard(object):

    def __init__(self, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9):

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

    def tiles(self):
        return self.tileList

    def can_move_up(self):
        if self.tile_zero.index in (3,4,5,6,7,8):
            return False
        else:
           return True

    def can_move_down(self):
        if self.tile_zero.index in (0,1,2,3,4,5):
            return False
        else:
            return True

    def can_move_left(self):
        if self.tile_zero.index in (1,2,4,5,7,8):
            return False
        else:
            return True

    def move_left(self):
        #find tile to left - TODO FOr loop
        # find tile with tile_zero.index-1 - increment
        self.tile_zero.move_left
        foundTile = self.tileList[3]
        foundTile.move_right()
        self.tile_zero.move_left()

    def move_right(self):
        self.tile_zero.move_right

    def move_up(self):
        self.tile_zero.move_up

    def move_down(self):
        self.tile_zero.move_down
      #  tileToMove = self.tileList.__getitem__()


    def show(self):
        sortedList = sorted(self.tileList, key=indexSort)
        print(sortedList[0].value, ",", sortedList[1].value, ",", sortedList[2].value )
        print(sortedList[3].value, ",", sortedList[4].value, ",", sortedList[5].value)
        print(sortedList[6].value, ",", sortedList[7].value, ",", sortedList[8].value, "\n")



def indexSort(Tile):
    return Tile.index

def CreateChildBoard(existingBoard):
    childList = sorted(existingBoard, key=indexSort)
    return TileBoard(childList[0], childList[1], childList[2], childList[3], childList[4], childList[5],
                     childList[6], childList[7], childList[8])


def CreateInitialBoard():
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

#myList3 = sorted(myList2 ,key=lamba Tile: Tile.index)
#myList3 = sorted(myList2, key=indexSort)

#board1 = TileBoard(0,1,2,3,4,5,6,7,8)
#board2 = TileBoard(3,4,5,1,0,2,6,7,8)

#board2 = board1.copy_board()

board1 = CreateInitialBoard()
board1.show()

board2 = CreateChildBoard(board1.tileList)
board2.show()

board3 = board2.move_up()
board3.show()

board4 = board2.move_down()
board4.show()
#board2 = CreateChildBoard(board1)
#board2.show()

#board2.show()

#board2.move_left()
#board2.show()

#print(board1.can_move_down())
#print(board2.can_move_down())