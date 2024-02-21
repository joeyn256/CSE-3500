# we are given an n * n matrix
#we have to start in top left and populate the matrix being able to move left right or down and finding the best sum ending in bottom right
def find_path(matrix):
    for i in range(len(matrix)): 
        for j in range(len(matrix)): # O(n^2) time with two for loops
            if j == 0: # base case is override the original matrix and set the first value in the row equal to the top value plus the old right value (so then we can compare the new values to something going left to right on the next row)
                grid[i][j] += max(matrix[i-1][j], matrix[i][j+1]) #this is very interesting logic that works out but we have to know how to follow and backtrack the matrix
            elif j == len(matrix)-1: #edge case if we reach the right value we only look at top and left
                grid[i][j] += max(matrix[i-1][j], matrix[i][j-1])
            else: # main case is to look at top left and right
                grid[i][j] += max(grid[i-1][j], grid[i][j-1], grid[i][j+1])
    return grid

#this function outputs the corresponding coords of the pathway and the total sum
def path(matrix,matrix2):
    n = len(matrix)

    total_sum = 0 #keep counter of max pathway

    pathway = [] # keep track of coords of best matrix
    
    i, j = n - 1, n - 1 # start from the bottom-right corner

    while i >= 0 and j >= 0:

        pathway.append((i,j)) #add coords
        total_sum = total_sum + matrix2[i][j] #update total sum

        if i == 0 and j == 0:
            break

        # checks which direction leads to the largest value whether that is up, left, right includes edge cases
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if matrix[i-1][j] > matrix[i][j-1]:
                i -= 1
            else:
                j -= 1

    return pathway[::-1], total_sum #flip list of tuples to get ideal pathway

if __name__ == '__main__':
    original_matrix = [[-5,10,-2,8],[3,-6,7,9],[-10,4,2,-3],[6,-8,1,0]]

    matrix = original_matrix # store a copy to manipulated

    c = find_path(matrix) # this overwrites matrix unfortunately so we stored a copy

    print(f'best pathway matrix: {c}')

    # traverses through the matrix
    pathway_matrix = path(c,original_matrix)

    # prints the pathway in a list of typles and the resulting sum
    print(f'resulting pathway of tuples: {pathway_matrix}')

