#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    char_counts=Counter(s)
    freq=Counter(char_counts.values())
    
    if len(freq)==1:
        return "YES"
    elif len(freq)==2:
        f1, c1=freq.popitem()
        f2, c2=freq.popitem()
        
        if(f1==1 and c1==1) or (f2==1 and c2==1):
            return "YES"
        if(abs(f1-f2)==1 and (c1==1 or c2==1)):
            if (c1==1 and f1>f2) or (c2==1 and f2>f1):
                return "YES"
            else:
                return "NO"
        else:
            return "NO"
    else: 
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
