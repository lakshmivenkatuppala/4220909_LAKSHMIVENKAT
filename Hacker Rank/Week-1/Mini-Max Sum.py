#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    Sum = 0
    Min = arr[0]
    Max = arr[0]
    for i in arr:
        Sum += i
        Min = min(i, Min )
        Max = max (i, Max )
    print ((Sum-Max), (Sum-Min))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
