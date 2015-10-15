#!/bin/python

#What is the value of the first triangle number to have over five hundred divisors?

import math

def findTriangle(x):
    triangle = 0
    for y in range(1,x+1):
        triangle += y
    return triangle

def countDivisors(x):
    count = 0
    for y in range(1,math.sqrt(x)):
        if x % y == 0:
            count += 1
    return count

number = input("Enter a number: ")

#number = 1000

"""while True:
    count = countDivisors(findTriangle(int(number)))
    print(number, count)
    if count > 500:
        break
    else:
        number += 1000
"""

print(findTriangle(int(number)))
print(countDivisors(int(number)))
