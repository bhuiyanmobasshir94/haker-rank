#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    parser_list = s.split(':')
    am_pm = parser_list[2][2:4]
    hour = parser_list[0]
    minute = parser_list[1]
    sec = parser_list[2][0:2]
    
    if am_pm == "AM":
        if hour == '12':
            hour_p = '00'
        else:
            hour_p = hour
        return ("%s:%s:%s"%(hour_p,minute,sec))     
    else:
        if hour == '12':
            hour_p = '12'
        else:
            hour_p = str(int(hour)+12)
        return ("%s:%s:%s"%(hour_p,minute,sec)) 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
