class Tile(object):
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value

    def move_left(self):
        self.column = self.column - 1

    def move_right(self):
        self.column = self.column + 1

    def move_up(self):
        self.row = self.row - 1

    def move_down(self):
        self.row = self.row + 1

    def is_empty_tile(self):
        return True if self.value == 0 else False

    def show(self):
        print("row: ", self.row, ", col: ", self.column, ", val: ", self.value)

class TileBoard(object):

    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8, value9):

        self.tileList = []
        self.tileList.append(Tile(0, 0, value1))
        self.tileList.append(Tile(0, 1, value2))
        self.tileList.append(Tile(0, 2, value3))
        self.tileList.append(Tile(1, 0, value4))
        self.tileList.append(Tile(1, 1, value5))
        self.tileList.append(Tile(1, 2, value6))
        self.tileList.append(Tile(2, 0, value7))
        self.tileList.append(Tile(2, 1, value8))
        self.tileList.append(Tile(2, 2, value9))
        for x in self.tileList:
            if x.value == 0:
                self.tile_zero = x


    def can_move_up(self):
        if self.tile_zero.row == 0:
            return False
        else:
           return True

    def can_move_down(self):
        if self.tile_zero.row == 2:
            return False
        else:
            return True

    def can_move_left(self):
        if self.tile_zero.column == 0:
            return False
        else:
            return True

    def move_left(self):
        #find tile to left - TODO FOr loop
        foundTile = self.tileList[3]
        foundTile.move_right()
        self.tile_zero.move_left()

    def copy_board(self):
        return TileBoard(self.tileList[0].value, self.tileList[1].value, self.tileList[2].value,
                         self.tileList[3].value, self.tileList[4].value,  self.tileList[5].value,
                         self.tileList[6].value, self.tileList[7].value, self.tileList[8].value)


    def show(self):
        print(self.tileList[0].value, ",", self.tileList[1].value, ",", self.tileList[2].value )
        print(self.tileList[3].value, ",", self.tileList[4].value, ",", self.tileList[5].value)
        print(self.tileList[6].value, ",", self.tileList[7].value, ",", self.tileList[8].value, "\n")




board1 = TileBoard(0,1,2,3,4,5,6,7,8)
#board2 = TileBoard(3,4,5,1,0,2,6,7,8)

#board2 = board1.copy_board()
#board1.show()
#board2.show()

#board2.move_left()
#board2.show()

#print(board1.can_move_down())
#print(board2.can_move_down())


