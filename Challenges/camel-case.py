"""Alice wrote a sequence of words in CamelCase as a string of letters, s, having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given s, print the number of words in s on a new line.

Sample Input

saveChangesInTheEditor

Sample Output

5
"""

s = raw_input().strip()

total = 1
for letter in s:
    if letter.istitle():
        total += 1
        
print total