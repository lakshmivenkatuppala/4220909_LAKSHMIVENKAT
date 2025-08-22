#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def ispalindrome(s, i, j):
    while i<j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

def palindromeIndex(s):
    # Write your code here
    start=0
    end=len(s)-1
    
    while start<end:
        if s[start] != s[end]:
            if ispalindrome(s, start+1, end):
                return start
            elif ispalindrome(s, start, end-1):
                return end
            else:
                return -1
        start += 1 
        end -= 1
    return -1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
