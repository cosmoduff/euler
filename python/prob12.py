#!/bin/python3

# What is the value of the first triangle number to have over five hundred divisors?

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
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
    square = math.sqrt(x)
    for y in range(1,int(square)):
        if x % y == 0:
            count += 1
    count = count * 2
    if square * square != x:
        return count
    else:
        return count + 1

number = 1

while True:
    triangle = genTriangle(number)
    if is_prime(triangle):
        number += 1
        continue
    else:
        count = countDivisors(int(triangle))
        if count > 500:
            print(triangle)
            break
        else:
            number += 1
