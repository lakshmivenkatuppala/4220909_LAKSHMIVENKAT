#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    curr_max, total_max=arr[0], arr[0]
    for i in range(1, len(arr)):
        curr_max=max(arr[i], curr_max+arr[i])
        total_max=max(curr_max, total_max)
    seq_sum=0
    for x in arr:
        if x>0:
            seq_sum += x
    if seq_sum ==0:
        seq_sum = max(arr)
    return total_max, seq_sum
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
