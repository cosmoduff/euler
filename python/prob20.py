#!/usr/bin/env python
# Find the sum of the digits in the number 100!

def factorial_exp(n):
    total = 1
    for x in range(1, n):
        total = total * x

    return total

def add_digits(n):
# Takes a number n and returns the sum of the digits of that number
# Ex 32768 3+2+7+6+8=26
    result = sum(list(map(int, str(n))))
    return result 

print(add_digits(factorial_exp(100)))
