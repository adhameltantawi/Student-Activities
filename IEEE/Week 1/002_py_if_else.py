# Problem: Python If-Else
# Link: https://www.hackerrank.com/challenges/py-if-else/problem
# Approach: Check parity and ranges to print the required label.
# Time Complexity: O(1)
# Space Complexity: O(1)

#problem 2
# https://www.hackerrank.com/challenges/py-if-else/problem
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1 :
        print('Weird')
    elif n % 2 ==0 and 2 <= n <5:
        print ('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')

