#!/bin/python

import math
import os
import random
import re
import sys

def staircase(n):
    
    for i in range(1,n+1):
        str=''
        for k in range(1,((n-i)+1)):
            str +=' '
        for j in range(1,i+1):
            str += '#'
        print(str)

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
