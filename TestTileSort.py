from TileBoard3 import *

tile1 = Tile(0,1)
tile2 = Tile(1,5)
tile3 = Tile(2,8)

tile4 = Tile(3,3)
tile5 = Tile(4,4)
tile6 = Tile(5,2)

myList = [tile1, tile2, tile3,tile4, tile5, tile6]

myList2 = [tile5, tile4, tile3,  tile6]

def indexSort(Tile):
    return Tile.index

#myList3 = sorted(myList2 ,key=lamba Tile: Tile.index)
myList3 = sorted(myList2, key=indexSort)

for t in myList3:
    print(t.index, ",", t.value)

