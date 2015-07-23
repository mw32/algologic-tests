#!/usr/bin/python

class Matrix():

    def __init__(self, rows=5, cols=5):
        self.cells = [[None for c in range(cols)] for r in range(rows)]

    def transpose(self):
        self.cells = list(map(list, zip(*self.cells)))

    def mirror(self):
        for row in self.cells:
            row.reverse()

    def invert(self):
        self.cells.reverse()

    def rotate(self, clockwise=True):
        self.transpose()
        self.mirror() if clockwise else self.invert()

    def iter_spiral(self, grid=None):
        grid = grid or self.cells
        next_grid = []
        for cell in reversed(grid[0]):
            yield cell
        for row in grid[1:-1]:
            yield row[0]
            next_grid.append(row[1:-1])
        if len(grid) > 1:
            for cell in grid[-1]:
                yield cell
        for row in reversed(grid[1:-1]):
            yield row[-1]
        if next_grid:
            for cell in self.iter_spiral(grid=next_grid):
                yield cell

    def show(self):
        for row in self.cells:
            print(row)

def test_matrix():
    m = Matrix()
    m.cells = [[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]]
    print("We expect the spiral to be:\n 4, 3, 2, 1, 5, 9, 13, 14, 15, 16, 12, 8, 7, 6, 10, 11")
    print("What the iterator yields:")
    for cell in m.iter_spiral():
        print('%s,' % cell),
    print("\nThe matrix looks like this:")
    m.show()
    print("Now this is how it looks rotated 90 deg clockwise")
    m.rotate()
    m.show()
    print("Now we'll rotate it back")
    m.rotate(clockwise=False)
    m.show()
    print("Now we'll transpose it")
    m.transpose()
    m.show()
    print("Inverting the above")
    m.invert()
    m.show()
    print("Mirroring the above")
    m.mirror()
    m.show()

if __name__ == '__main__':
    test_matrix()
