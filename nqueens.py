#!/usr/bin/python
BOARD_SIZE = 4
 
def under_attack1(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))
    # abs(col - x) = distance from new column (col) to column of queen (x)
    # len(queens) - i = distance of diagonal reach at row n calculated based on
    #     distance from length of set of queens subtracted by iteration index i
 
def under_attack(col, queens):
    # This calculates the other way around, from the current column if any
    # previous queens lies in right, left or col, going backwards,
    # hence reversed
    left = right = col
    for r, c in reversed(list(enumerate(queens))):
        left, right = left - 1, right + 1
        if c in (left, col, right):
            return True
    return False

def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = [solution+[i+1]
                       for solution in solutions
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution)]
    print solutions
    return solutions
 
for answer in solve(BOARD_SIZE): print(list(enumerate(answer, start=1)))
