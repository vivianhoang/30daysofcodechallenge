"""Alice owns a company that transports tour groups between two islands.
She has n trips booked, and each trip has i passengers. Alice has m boats for
transporting people, and each boat's maximum capacity is c passengers.

Given the number of passengers going on each trip, determine whether or not
Alice can perform all  trips using no more than m boats per individual trip.
If this is possible, print Yes; otherwise, print No.

n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

Sample Input 1

5 1 2
1 2 1 4 1
Sample Output 1

No
Explanation 1

Alice has m=2 boats and a maximum capacity of c=1 passenger per boat. This
means she can transport at most c=1 passengers at a time.

There are n=5 tour groups, and the largest tour group contains p=4 passengers.
Because Alice does not have enough boats to transport a group of four passengers, we print No.
"""

n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))

highest = max(p)

if highest > c*m:
    print "No"
else:
    print "Yes"