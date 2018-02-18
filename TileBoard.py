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



