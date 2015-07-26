#!/usr/bin/python

def find_paths(graph, start, path, allpaths, dmax):
    if dmax == 0:
        allpaths.append([start])
    else:
        newpath = path + [start]
        for edge in graph[start]:
            d = graph[start][edge]
            if dmax - d >= 0:
                find_paths(graph, edge, newpath, allpaths, dmax - d)
            else:
                allpaths.append(newpath + [edge])
    return allpaths

graph = { 
          1: {2: 33, 3: 15},
          2: {1: 33, 4: 57, 5: 7},
          3: {1: 15},
          4: {2: 57},
          5: {1: 89, 2: 7},
        }

print find_paths(graph, 1, [], [], 50)
