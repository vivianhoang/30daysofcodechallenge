"""Task 
Given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).

Note: 0 is considered to be an even index.

Sample Input

2
Hacker
Rank
Sample Output

Hce akr
Rn ak"""

num = int(raw_input())

i = 0
input_lst = []
while i < num:
    word = raw_input()
    input_lst.append(word)
    i += 1

evens = []
odds = []

for word in input_lst:
    for i in range(len(word)):
        if i%2 == 0:
            evens.append(word[i])
        elif i%2 != 0:
            odds.append(word[i])
    print "".join(evens), "".join(odds)
    del evens[:]
    del odds[:]