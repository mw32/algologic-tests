#!/usr/bin/python
import time

def spiral(n):
    limit = n*n
    matrix = [n*[0] for i in range(n)] 
    d = r = c = 0
    val = 1
    # Dir in (row,col) tuple in each direction: top, right, bottom, left
    #dir = [ (0,1), (1,0), (0,-1), (-1,0) ] 
    dir = [ {'r':0,'c':1}, {'r':1,'c':0}, {'r':0,'c':-1}, {'r':-1,'c':0} ]

    while val <= limit:
        print r,c,val
        matrix[r][c] = val
        val += 1
        r += dir[d]['r']
        c += dir[d]['c']
        if invalid(matrix, r, c):
            r -= dir[d]['r']
            c -= dir[d]['c']
            d = (d + 1) % 4
            print "INVALID! Change direction %s."%dir[d]
            r += dir[d]['r']
            c += dir[d]['c']
    pprint(matrix)

def invalid(matrix, r, c):
    return r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix) or matrix[r][c] != 0

def pprint(matrix):
    for row in matrix:
        for val in row:
            print '{:4}'.format(val),
        print

if __name__ == '__main__':
    n = input("Enter array row/column (single number): ")
    spiral(n)
