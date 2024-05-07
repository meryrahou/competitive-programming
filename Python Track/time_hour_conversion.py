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
    hh, mm, ss, indicator = s[:2], s[3:5], s[6:8], s[8:]

    if indicator == 'PM' and hh != '12':
        hh = str(int(hh) + 12)
    elif indicator == 'AM' and hh == '12':
        hh = '00'

    return f"{hh}:{mm}:{ss}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
