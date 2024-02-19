import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=True):
        
        matrix = [] #this will be how the matrix is stored in list in a list ex: [[3,2,1],[7,6,5],...[n,n,n]]

        firstrow = [] 
    
        for i in range(self.width): # store first row
            firstrow.append(self.energy(0,i))
        matrix = [firstrow]

        for j in range(1, self.height): #iterate from 2nd row to end
            visited = []
            for i in range(self.width):
                # energy calculation, flip j and i to get the correct elements for matrix[][]
                if i == 0:
                    current_energy = self.energy(i, j) + min( #edge case don't look at i - 1 if at 0
                    matrix[j-1][i],
                    matrix[j-1][i+1]
                    )
                if i == self.width - 1:
                    current_energy = self.energy(i, j) + min( # edge case don't look at i + 1 if on self.width - 1
                    matrix[j-1][i-1],
                    matrix[j-1][i]
                    )
                else:
                    current_energy = self.energy(i, j) + min( # main cases: E(i, j) + min(M(i-1, j-1), M(i, j-1), M(i+1, j-1)) 
                    matrix[j-1][i-1],
                    matrix[j-1][i],
                    matrix[j-1][i+1]
                    )
                visited.append(current_energy) # add list to list
            matrix.append(visited)

        # time to construct the best seam path
    
        seam_value = float('inf') 

        for i in range(self.width): #iterate through all values in the last row
            if matrix[self.height - 1][i] < seam_value:
                seam_index = i 
                seam_value = matrix[self.height - 1][i] 

        seam = [(seam_index, self.height - 1)] #store min in new matrix

        for j in range(self.height - 2, -1, -1): #retrace through the matrix from bottom to top
            left = max(seam_index - 1, 0)
            right = min(seam_index + 1, self.width - 1)
            
            min_index = min((left, seam_index, right), key=lambda x: matrix[j][x]) # min function stores the new seam_index
            seam_index = min_index
            
            seam.append((seam_index, j)) # add the coordinates to the list
        
        return seam[::-1] # reverse order to produce in the correct order
    


    def naive(self):
        # helper function
        def best_seam(x, y):
            if y == self.height - 1: 
                return [(x, y)]

            seam_index = x
            seam_value = float('inf')

            # look at pathways left, center, and right
            for path in [-1, 0, 1]:
                new_x = x + path
                if 0 <= new_x < self.width:
                    seam = best_seam(new_x, y + 1)
                    total_energy = sum(self.energy(i, j) for i, j in seam) #total sum of each pathway
                    if total_energy < seam_value:
                        seam_value = total_energy
                        seam_index = new_x

            # start with the minimum pixel and use recursion
            return [(x, y)] + best_seam(seam_index, y + 1) # call helper

        # recursively search every pathway for every pixel starting in the top row and choose minimum pathway
        min_seam = None

        seam_value = float('inf')
        for x in range(self.width):
            seam = best_seam(x, 0)
            total_energy = sum(self.energy(i, j) for i, j in seam)
            if total_energy < seam_value:
                seam_value = total_energy
                min_seam = seam

        return min_seam #no need to reverse order since we start from the top
