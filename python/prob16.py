# What is th sum of the digits of the number 2^1000?

import math

num = 2**1000

def add_digits(n):
# Takes a number n and returns the sum of the digits of that number
# Ex 32768 3+2+7+6+8=26
    sum = 0

    for x in str(n):
        sum += int(x)

    return sum

print(add_digits(num))
