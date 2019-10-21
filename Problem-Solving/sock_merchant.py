#!/bin/python

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    unique_socks = Counter()
    pair_counts = 0
    if len(ar) == n:
        for i in ar:
            unique_socks[i] += 1
        
        for elem, cnt in list(unique_socks.most_common()):
            pair = cnt // 2
            if pair:
                pair_counts += pair
    return pair_counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
