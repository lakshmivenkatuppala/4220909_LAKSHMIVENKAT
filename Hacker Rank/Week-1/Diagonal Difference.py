#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    l=len(arr)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(l):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][l-i-1]
    diagonal_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
    return diagonal_difference
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
