class BoardState(object):

    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

        def __eq__(self, other):
            return self.row1 == other.row1 and self.row2 == other.row2 and self.row3 == other.row3

        def __ne__(self, other):
            return  self.row1 != other.row1 or self.row2 != other.row2 or self.row3 != other.row3



board1 = BoardState([0, 1, 2], [3, 4, 5], [6, 7, 8])
board2 = BoardState([0, 1, 2], [3, 4, 5], [6, 7, 8])
board3 = BoardState([0, 1, 2], [6, 7, 8], [3, 4, 5])

print(board1 == board2)
print(board1.row1 == board2.row1)
print(board1.row2 == board2.row2)
print(board1.row3 == board2.row3)





