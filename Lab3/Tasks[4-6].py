#!/usr/bin/env python
# coding: utf-8

""" Task 4

    Calculate N! (factorial)"""


n = int(input("Enter any natural number: "))
f = n*(n-1)
i = 2
while i<n:
    f = f*(n-i)
    i+=1
print(f)


""" Task 5

    Check if the number is prime"""


n = int(input("Enter an integer > 1: "))
for i in range(2, n):
    if n % i == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
        


""" Task 6

    Calculate number e"""


from math import factorial

def euler(n):

"""
    This function calculates the value of euler number.
"""
    euler = 1
    n = 100
    for k in range(1, n+1):
        euler = euler + 1/factorial(k)
    return print(euler)

euler(100)
