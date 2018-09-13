#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    total, temp = 0, 0
    lenS = len(s)
    num = n / lenS
    wholeNum = n//lenS 
    fraction = num - wholeNum
    if n < len(s):
        for i in range(n):
            if s[i] == 'a':
                total+=1
    else:
        for i in range(lenS):
            if s[i] == 'a':
                temp+=1
        total = temp*wholeNum
        remaining = round(fraction*lenS)
        for i in range(remaining):
            if s[i] == 'a':
                total+=1
    return total
    
               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
