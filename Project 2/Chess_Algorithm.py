def fill_bd(bd, i, j, size):
    # base case
    if size == 2:
        # place the pieces in remaining squares
        for x in range(i, i + size):
            for y in range(j, j + size):
                if bd[x][y] != -1:  # left square reached
                    bd[x][y] = 1
        
        #print matrix at each occurence to see it filling correctly
        for squares in bd:
            for square in squares:
                print(square, end=' ')
            print() # new line for each row
        print()  # new line for each matrix
        
        return #end recursion instance

    #put L-shaped piece in the middle of the four quadrants on the board
    bd[i + size // 2][j + size // 2] = 1
    bd[i + size // 2 - 1][j + size // 2] = 1
    bd[i + size // 2 - 1][j + size // 2 - 1] = 1
    
    #print matrix at each occurence to see it filling correctly
    for squares in bd:
        for square in squares:
            print(square, end=' ')
        print() 
    print()

    #split the board into four quadrants and put an L-shaped piece in the middle of the board and then split again
    #recursively solving the four quadrant sub problems until we reach the base case 2x2 matrix
    fill_bd(bd, i, j, size // 2)
    fill_bd(bd, i + size // 2, j, size // 2)
    fill_bd(bd, i, j + size // 2, size // 2)
    fill_bd(bd, i + size // 2, j + size // 2, size // 2)

k = int(input('enter k value: '))
bd = [[0 for i in range(2**k)] for j in range(2**k)]

# remove the top left corner square
bd[0][0] = -1
fill_bd(bd, 0, 0, 2**k)