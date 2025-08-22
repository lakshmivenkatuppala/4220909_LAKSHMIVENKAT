#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    # Write your code here
    r=len(grid)
    c==len(grid[0])
    if n==1:
        return grid
    elif n%2==0:
        return ["O" * c for _ in range(r)]
    first=detonate(grid)
    second=detonate(first)
    if(n-3)%4==0:
        return first
    else:
        return second
def detonate(grid):
    r=len(grid)
    c=len(grid[0])
    new_grid=[["O"]*c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if grid[i][j]=="O":
                new_grid[i][j]="."
                if i>0: new_grid[i-1][j]="."
                if i<r-1: new_grid[i+1][j]="."
                if j>0: new_grid[i][j-1]="."
                if j<c-1: new_grid[i][j+1]="."
    return ["".join(row) for row in new_grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
