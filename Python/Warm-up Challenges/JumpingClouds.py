#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    minJump = 0
    index = 0
    while(index+1<len(c)):
        if index+2 < len(c): 
            if c[index+2] == 0:#you can jump 2
                minJump+=1
                index+=2
            else: #You can't jump 2
                minJump+=1
                index+=1
        else:
            minJump+=1
            index+=1
    return minJump
        
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
