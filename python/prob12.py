#!/bin/python

#What is the value of the first triangle number to have over five hundred divisors?

import math

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
    trianlge = genTriangle(number)
    count = countDivisors(int(number))
    print(number, count)
    if count > 500:
        break
    else:
        number += 1
# notes
# add prime check to quickly move on as a prime only has two divisors
