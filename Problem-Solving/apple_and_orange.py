#!/bin/python

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_in_range = len(list(x for x in apples if (a+x) >= s and (a+x) <=t ))
    oranges_in_range = len(list(x for x in oranges if (b+x) >= s and (b+x) <=t ))
    print(apples_in_range)
    print(oranges_in_range)
    
if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    countApplesAndOranges(s, t, a, b, apples, oranges)
