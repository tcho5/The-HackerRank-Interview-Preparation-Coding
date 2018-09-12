#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    valid = True
    for i in range(n):
        if i+1 < len(ar):
            if ar[i] == ar[i+1]:
                if valid == True:
                    valid = False
                    pairs +=1
                else:
                    valid = True
            else:
                valid = True
    return pairs
                        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
