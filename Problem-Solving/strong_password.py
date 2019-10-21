#!/bin/python

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    count = 0
    cases = [r'[a-z]', r'[A-Z]', r'[\d]', r'[!@#$%^&*()\-+]']
    for case in cases:
        if not re.search(case, password):
            count += 1

    return max(count, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
