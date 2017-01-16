"""Write a program that prints a staircase of size n.

Input Format

A single integer, n, denoting the size of the staircase.

Output Format

Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input

6 

Sample Output

     #
    ##
   ###
  ####
 #####
######
"""

counter = 1
n = int(raw_input().strip())

spaces = n - 1
for i in range(n):
    print (" " * (spaces)) + ("#" * counter)
    spaces -= 1
    counter += 1