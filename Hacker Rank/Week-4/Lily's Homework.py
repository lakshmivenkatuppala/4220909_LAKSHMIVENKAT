#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    def min_swaps(target):
        a = arr[:]  
        ind = {v: i for i, v in enumerate(a)}
        s = 0
        for i in range(len(a)):
            val = target[i]
            if a[i] != val:
                s += 1
                swap_idx = ind[val]
                a[i], a[swap_idx] = a[swap_idx], a[i]
                ind[a[swap_idx]] = swap_idx
                ind[a[i]] = i
        return s

    arr1 = sorted(arr)
    arr2 = arr1[::-1]

    return min(min_swaps(arr1), min_swaps(arr2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
