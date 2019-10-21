#!/bin/python

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    n = len(arr)
    sum_list = list()
    for index in range(0,n):
        new_arr = arr.copy()
        new_arr.pop(index)
        sum_list.append(sum(new_arr))
    print(min(sum_list),max(sum_list))

if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
