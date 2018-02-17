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




goalState = [[0,1,2],[3,4,5],[6,7,8]]

boardInput = [[2,1,0],[3,4,5],[6,7,8]]

boardInput2 = [[3,4,5],[2,1,0],[6,7,8]]

newBoard = move_up_row(boardInput2[0],boardInput2[1], boardInput2[2])

print(boardInput)
print(newBoard)

