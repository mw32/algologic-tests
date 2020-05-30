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
        MARKER = 66666

        print(matrix)

        #############
        # BRUTE FORCE - O(m*n)
        #############
        
        # First loop to find 0s and set markers in the row/col
        for i in range(rownum):
            for j in range(colnum):
                print("[%d][%d]"%(i,j))

                # For any 0 element, need to add marker AND set corresponding row/col to 0s
                if (matrix[i][j] == 0):
                    print("processing [%d][%d] = %d - Zero!" %(i, j, matrix[i][j]))

                    for x in range(colnum):
                        if (matrix[i][x] == 0 or matrix[i][x] == MARKER):
                            print("row: already [%d][%d] = %d"%(i,x,matrix[i][x]))
                        else:
                            print("row: setting [%d][%d] = %d -> MARKER"%(i,x,matrix[i][x]))
                            matrix[i][x] = MARKER
                        print("[%d][%d] matrix: %s"%(i,j,matrix))

                    for x in range(rownum):
                        if (matrix[x][j] == 0 or matrix[x][j] == MARKER):
                            print("col: already [%d][%d] = %d"%(x,j,matrix[x][j]))
                        else:
                            print("col: setting [%d][%d] = %d -> MARKER"%(x,j,matrix[x][j]))
                            matrix[x][j] = MARKER
                        print("[%d][%d] matrix: %s"%(i,j,matrix))
                      
                    print("[%d][%d] matrix: %s"%(i,j,matrix))

        # Second pass to flip markers to 0
        for i in range(rownum):
            for j in range(colnum):
                matrix[i][j] = 0 if matrix[i][j] == MARKER else matrix[i][j]
                
        return(matrix)
      

#M = [[0, 1, 2, 5], [4, 2, 1, 4], [0, 4, 3, 3]]
#M = [[1,0,3]]
#M = [[1,2,0],[0,3,1],[3,4,5]]
#M = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
M = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
s = Solution()
print(s.setZeroes(M))