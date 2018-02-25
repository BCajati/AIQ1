from TileBoard3 import *

board1 = CreateInitialBoard()
board1.show()
#for tile in board1.tileList:
 #  print(tile.index,",", tile.value )

print("move right")
board1.move_right()
board1.show()

#for tile in board1.tileList:
 #   print(tile.index,",", tile.value )

print ("move left")
board1.move_left()
board1.show()
#for tile in board1.tileList:
#    print(tile.index,",", tile.value )

print("move down")
board1.move_down()
board1.show()

print ("move up")
board1.move_up()
board1.show()

print("move right")
board1.move_right()
board1.show()

print("move down")
board1.move_down()
board1.show()


