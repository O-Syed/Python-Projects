#!/bin/python3

import math
import os
import random
import re
import sys



valid = re.compile("\w")
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
# print(first_multiple_input, n, m)
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

mystr = ''
temp = ''
space = ''
flag = True
for m in range(m):
    for i in matrix:
        while valid.match(i[m]):
            while flag:
                mystr += temp
                flag = False
                space=''
                break
            mystr += space
            mystr += i[m]
            temp = ''
            space = ''
            break
        while not valid.match(i[m]):
            space = ' '
            temp += i[m]
            break
mystr += temp
print(mystr)
