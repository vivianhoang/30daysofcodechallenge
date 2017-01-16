"""You are given an array of integers of size N.
You need to print the sum of the elements in the array,
keeping in mind that some of those integers may be quite large."""

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

total = 0 

for num in arr:
    total += num
    
print total