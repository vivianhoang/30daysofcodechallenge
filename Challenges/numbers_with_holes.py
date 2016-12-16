"""Raj has solved the puzzle below:

24 -> 1
1264 -> 2
9899 -> 5
349 -> x

Raj determined that the puzzle can be solved by counting the number of holes in the digits of a number. e.g. 1,2,3,5,7 have no holes, 0, 4, 6,
9 have 1 hole each, and 8 has 2 holes. 2 is therefore the value of x to the last line.

Excited by this discovery, Raj now wants to solve this puzzle using a computer program. You have to write a function whose signature is
solvePuzzle(int num) where num is the input integer, and the return value is the number of holes in num.

Constraints:
1 ≤ num ≤ 10
There will be no leading zeroes.

Sample Input #0:
630
Sample Output #0:
2
"""

def solvePuzzle(num):
    total = 0
    num_holes = {"0": 1, "4": 1, "6": 1, "8":2 , "9":1,}

    converted_num = str(num)
    for i in converted_num:
        if i in num_holes:
            total += num_holes[i]

    print total
