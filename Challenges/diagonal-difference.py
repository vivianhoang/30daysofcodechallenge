"""Given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

Sample Input:

3
11 2 4
4 5 6
10 8 -12

Sample Output:

15

Explanation:

The primary diagonal is: 
11
      5
            -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
            4
      5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19 
Difference: |4 - 19| = 15
"""

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

count = 0
totalA = 0
totalB = 0
for i in a:
    totalA += i[count]
    count += 1

# count is now at largest length of matrix + 1

count -= 1
for j in a:
    totalB += j[count]
    count -= 1
    
print abs(totalA-totalB)