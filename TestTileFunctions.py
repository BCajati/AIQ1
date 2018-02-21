from TileBoard2 import *

tile1 = Tile(0,0,1)
tile1.show()


tile1.move_right()
tile1.show()

tile1.move_down()
tile1.show()

print(tile1.is_empty_tile())

tile2 = Tile(1,1,0)
print(tile2.is_empty_tile())