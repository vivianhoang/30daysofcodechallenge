"""
Task 
Given an array of integers, print the elements in reverse order as
a single line of space-separated numbers.
"""

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

rev_arr = arr[::-1]

for i in rev_arr:
    print i,