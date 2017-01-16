"""
Task 
Given an array of integers, print the elements in reverse order as
a single line of space-separated numbers.
"""

n = int(input())
name_numbers = []
phone_book = {}
count = 0

for i in range(n):
    name_numbers.append(raw_input().split(" "))

for j in name_numbers:
    phone_book[name_numbers[count][0]] = name_numbers[count][1]
    count += 1

while True:
    try:
        name = raw_input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break