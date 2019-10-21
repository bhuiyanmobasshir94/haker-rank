#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    count = 0
    for i, v in enumerate(list(s)):
        if v.isupper() and i != 0:
            count += 1
    print(count +1)
    
if __name__ == '__main__':
   
    s = input()

    camelcase(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
