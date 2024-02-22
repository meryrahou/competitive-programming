#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    awardA = 0
    awardB = 0
    for i in range(len(a)):
        if a[i] > b[i]: awardA +=1
        if a[i] < b[i]: awardB +=1
    
    return [awardA , awardB]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
