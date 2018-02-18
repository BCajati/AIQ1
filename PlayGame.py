def move_up_row(row1, row2, row3):
    if 0 in row2:
        # swap the zero from row2 to row1
        index = row2.index(0)
        swap_row1 = row1[index]
        print(swap_row1)
        swap_row2 = row2[index]
        print(swap_row2)
        row1[index] = swap_row2
        print(row1)
        row2[index] = swap_row1
        print(row2)
    return [row1,row2,row3]

def canMoveRight(row):
    zeroIndex = row.index(0)
    if zeroIndex != 2:
        return True
    else:
        return False

def move_right(row):
    index = row.index(0)
    item0 = row[0]
    item1 = row[1]
    item2 = row[2]
    newrow = list(row)

    if index == 0:
        newrow[0] = item1
        newrow[1] = item0
    elif index == 1:
        newrow[1] = item2
        newrow[2] = item1

    print(row)
    print(" right ->")
    print(newrow)
    print("\n")
    return newrow

def canMoveLeft(row):
    zeroIndex = row.index(0)
    if zeroIndex != 0:
        return True
    else:
        return False

def move_left(row):
    index = row.index(0)
    item0 = row[0]
    item1 = row[1]
    item2 = row[2]
    newrow = list(row)

    if index == 1:
        newrow[1] = item0
        newrow[0] = item1
    elif index == 2:
        newrow[2] = item1
        newrow[1] = item2

    print(row)
    print(" left <-")
    print(newrow)
    print("\n")

    return newrow


#test board movements

goalState = [[0,1,2],[3,4,5],[6,7,8]]



boardInput = [[2,1,0],[3,4,5],[6,7,8]]

newBoard = move_up_row(boardInput[0],boardInput[1], boardInput[2])

#print(boardInput)
#print(newBoard)

testRow1 = [0,1,2]
testRow2 = [1,0,2]
testRow3 = [2,1,0]


move_right(testRow1)
move_right(testRow2)
move_right(testRow3)

move_left(testRow1)
move_left(testRow2)
move_left(testRow3)

