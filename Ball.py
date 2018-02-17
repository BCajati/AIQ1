class Ball(object):

    def __init__(self, color, row1, row2):
        self.color = color
        self.row1 = row1
        self.row2 = row2

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.color == other.color and self.row1 == other.row1 and self.row2 == other.row2

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.color != other.color or self.row1 != other.row1 or self.row2 != other.row2


ball1 = Ball('blue', [0,1,2], [3,4,5])
ball2 = Ball('blue', [0,1,2], [3,4,5])
ball3 = Ball('green', [0,1,2], [3,4,5])
ball4 = Ball('blue',  [3,4,5], [3,4,5])


print(ball1 == ball2)  # Prints True :)
print(ball1 == ball3)  # Prints False :)
print(ball1 == ball4)