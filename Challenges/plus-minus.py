"""Given an array of integers, calculate which fraction of its elements are positive, which fraction of
its elements are negative, and which fraction of its elements are zeroes, respectively.
Print the decimal value of each fraction on a new line.

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.

Sample Input

6
-4 3 -9 0 4 1     

Sample Output

0.500000
0.333333
0.166667"""

from __future__ import division
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

pos = 0
neg = 0
zero = 0

for num in arr:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print float(pos/n)
print float(neg/n)
print float(zero/n)
