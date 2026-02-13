#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
MOD = 10**9+7

def legoBlocks(n, m):
    # Write your code here
    r=[0]*(m+1)
    r[0]=1
    for i in range(1, m+1):
        for j in (1,2,3,4):
            if i-j>=0:
                r[i]=(r[i]+r[i-j])%MOD
    t=[0]*(m+1)
    for i in range(1,m+1):
        t[i]=pow(r[i], n, MOD)
    s=[0]*(m+1)
    for i in range(1,m+1):
        x=0
        for y in range(1,i):
            x=(x+s[y]*t[i-y])%MOD
        s[i]=(t[i]-x+MOD)%MOD
    return s[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
