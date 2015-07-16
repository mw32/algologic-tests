#!/usr/bin/python

'''
   Map in form of matrix with distance in between
   from\to:    A    B    C    D
'''
dist = {
        'A': [-1,   5,  -1,   2],  # A to A, A to B, A to C, etc...
        'B': [-1,  -1,   3,   7],
        'C': [ 6,   8,  -1,   4],
        'D': [ 2,  -1,   3,  -1],
       }
 
def load_map():
    map = {}
    k = sorted(dist.keys())
    for i in dist:
        t = {}
        for j in range(len(dist[i])):
            t[k[j]] = dist[i][j]
        map[i] =  t

    print "%s" % map


if __name__ == '__main__':
    load_map()
