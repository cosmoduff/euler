#! /usr/bin/env python
#What is the 10001st prime number?

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
                return False
        i = i + 6
    return True

i = 0
number = 0

while i < 10001:
    number +=1
    if is_prime(number):
        i += 1

print(number, "is the 10001st prime")
