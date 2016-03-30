#!/bin/python

#What is the value of the first triangle number to have over five hundred divisors?

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i == 5
    while i * i <=n:
        if n % i == 0 or n % (i + 2) == 0:
                return False
        i = i + 6
    return True

def genTriangle(x):
    triangle = (x*(x+1))/2
    return triangle

def countDivisors(x):
    count = 0
    for y in range(1,int(math.sqrt(x))):
        if x % y == 0:
            count += 1
    return count

#number = input("Enter a number: ")

number = 1

while True:
    triangle = genTriangle(number)
    count = countDivisors(int(triangle))
    # print(number, count)
    if count > 5:
        print(triangle)
        break
    else:
        number += 1
# notes
# add prime check to quickly move on as a prime only has two divisors
