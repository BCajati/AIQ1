class TileBoard(object):
    def __init__(self, value1, value2, value3, value4, value5, value6, value7, value8, value9):
        tileList = []
        tileList.append(Tile(0, 0, value1))
        tileList.append(Tile(0, 1, value2))
        tileList.append(Tile(0, 2, value3))
        tileList.append(Tile(1, 0, value4))
        tileList.append(Tile(1, 1, value5))
        tileList.append(Tile(1, 2, value6))
        tileList.append(Tile(2, 0, value7))
        tileList.append(Tile(2, 1, value8))
        tileList.append(Tile(2, 2, value9))

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
            self.row = self.row -1

        def move_down(self):
            self.row = self.row + 1

        def is_empty_tile(self):
            return True if self.value == 0 else False

        def show(self):
            print("row: ", self.row, ", col: ", self.column, ", val: ", self.value)



def CreateBoard(value1, value2, value3, value4, value5, value6, value7, value8, value9):
    tileList = []

    return tileList






