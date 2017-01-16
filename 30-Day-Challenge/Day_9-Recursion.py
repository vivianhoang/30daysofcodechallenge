""" Task 
Write a factorial function that takes a positive integer,
N as a parameter and prints the result of N( factorial). """

num = int(raw_input())

def factorial(n):
    if n == 1:
        return 1
    for number in range(n):
        return n * factorial(n-1)
    
print factorial(num)