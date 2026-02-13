#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

from collections import deque

def solve(arr, queries):
    result = []
    n = len(arr)

    for q in queries:
        dq = deque()
        c = float('inf')
        for j in range(q):
            while dq and arr[dq[-1]] <= arr[j]:
                dq.pop()
            dq.append(j)
        c = arr[dq[0]]
        for j in range(q, n):
            if dq and dq[0] <= j - q:
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[j]:
                dq.pop()
            dq.append(j)
            c = min(c, arr[dq[0]])
        result.append(c)

    return result
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
