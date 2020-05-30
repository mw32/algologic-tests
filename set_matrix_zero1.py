#!/usr/bin/python

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.


class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rownum = len(matrix)
        colnum = len(matrix[0])

        is_col = False
        
#        print(matrix)

        #############
        # EFFICIENT - O(1)
        #############
        for i in range(rownum):
            if (matrix[i][0] == 0 and not is_col):
                # Special case: first col
#                print("SPE col: setting is_col = True")
                is_col = True

            for j in range(1,colnum):
#                print("[%d][%d]"%(i,j))
                
                if (matrix[i][j] == 0):
#                    print("[%d][%d] processing: Zero!"%(i,j))
#                    print("row: setting [%d][0] = %d -> 0"%(i,matrix[i][0]))
#                    print("col: setting [0][%d] = %d -> 0"%(j,matrix[0][j]))
                    matrix[i][0] = matrix[0][j] = 0

                print("[%d][%d] matrix: %s"%(i,j,matrix))

        for i in range(1,rownum):
            for j in range(1,colnum):
                if (not matrix[i][0] or not matrix[0][j]):
                    matrix[i][j] = 0
                    
                                        
        if (not matrix[0][0]):  # set first row to 0s
            for k in range(0,colnum):
                matrix[0][k] = 0
                
        if (is_col):
            for k in range(0,rownum):
                matrix[k][0] = 0
            

#                    # Setting all past row/col to 0s, unless it's already 0 or it's a marker row/col previously set to 0
#                    for a in range(0,i):
#                        if (matrix[a][j] == 0):
#                            print ("already [%d][%d] = 0"%(a,j))
#                            if (a == 0):
#                                print ("SPECIAL case marker row [%d][%d] = 0 -> MARKER"%(a,j))
#                                self.addMarker(a,j,matrix,markers)
#                        elif (matrix[a][j] != self.MARKER):
#                            print("setting [%d][%d] = 0"%(a,j))
#                            matrix[a][j] = 0
#
#                    for b in range(0,j):
#                        if (matrix[i][b] == 0):
#                            print ("already [%d][%d] = 0"%(i,b))
#                            if (b == 0):
#                                print ("SPECIAL case marker col [%d][%d] = 0 -> MARKER"%(a,j))
#                                self.addMarker(i,b,matrix,markers)
#                        elif (matrix[i][b] != self.MARKER):
#                            print("setting [%d][%d] = 0"%(i,b))
#                            matrix[i][b] = 0
#
#                # For non-zero, check if there's a marker in that row/col
#                else:
#                    # If not in marker row/col
#                    if (i != 0 and j != 0):                        
#                        if (matrix[i][0] == self.MARKER):
#                            print("processing [%d][%d] = %d => 0 - Marker! [%d][0]"%(i,j,matrix[i][j],i))
#                            matrix[i][j] = 0
#                        elif (matrix[0][j] == self.MARKER):
#                            print("processing [%d][%d] = %d => 0 - Marker! [0][%d]"%(i,j,matrix[i][j],j))
#                            matrix[i][j] = 0
#                    # else in marker row/col 
#                    # - check if corner top left is 0 indicates there was a 0 in marker row/col
#                    # - check if corner top left is a marker - which means corner itself was a 0 
#                    else:
#                        if (matrix[0][0] == self.MARKER):
#                            print("processing [%d][%d] = %d => 0 - Corner Marker! %d"%(i,j,matrix[i][j],matrix[0][0]))
#                            matrix[i][j] = 0
#
#        # Finally set the marker row/col to 0s
#        for i,j in markers:
#            matrix[i][j] = 0

        return(matrix)
      


M = [[0, 1, 2, 5], [4, 2, 1, 4], [0, 4, 3, 3]]
M = [[1,0,3]]
M = [[1,2,0],[0,3,1],[3,4,5]]
M = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
M = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]

s = Solution()
print(s.setZeroes(M))