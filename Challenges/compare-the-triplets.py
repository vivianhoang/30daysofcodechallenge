"""Comparing scores from Alice and Bob, print two space-separated integers earned by each.
If Alice's score is better than Bob's score, Alice get's a point, and vice versa.
Continue to do this with all their scores.
"""

A = map(int, raw_input().strip().split(' '))
B = map(int, raw_input().strip().split(' '))

alice = 0
bob = 0

for i in range(len(A)):
    if A[i] > B[i]:
        alice +=1
    elif A[i] < B[i]:
        bob += 1

print alice, bob
        