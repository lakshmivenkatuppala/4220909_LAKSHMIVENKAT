import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    N_ve = 0
    P_ve = 0
    Z_ro = 0
    S_ze = len(arr)
    
    for i in arr:
        if i>0:
            P_ve += 1
        elif i<0:
            N_ve += 1
        else:
            Z_ro += 1
    print(f"{(P_ve/S_ze):.6f}")
    print(f"{(N_ve/S_ze):.6f}")
    print(f"{(Z_ro/S_ze):.6f}")
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)