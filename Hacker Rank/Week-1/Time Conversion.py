#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hrs, mins, sec, a_p = re.findall('\d+|\w+', s)
    hrs=int(hrs)
    if a_p == 'AM' and hrs == 12:
        hrs = 0
    elif a_p == 'PM' and hrs != 12:
        hrs += 12
    return f'{hrs:02d}:{mins}:{sec}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
