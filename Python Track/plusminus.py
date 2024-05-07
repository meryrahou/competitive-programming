#!/bin/python3

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
l = [0,0,0]
def plusMinus(arr):
    # Write your code here
    for i in arr:
        if i > 0:    l[0] += 1
        elif i < 0:  l[1] += 1
        elif i == 0: l[2] += 1
    length = len(arr)
    print(f"{l[0]/ length:.6f}")
    print(f"{l[1]/ length:.6f}")
    print(f"{l[2]/ length:.6f}")
  
  
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
