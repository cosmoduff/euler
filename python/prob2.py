#!/usr/bin/env python
#By considering the terms in the Fibonacci sequence whose values do not exceed four million find the
#sum of the even-valued terms

first_number = 1
second_number = 1
fib = 0
total = 0

while fib < 4000000:
    fib = first_number + second_number
    if fib % 2 == 0:
        total += fib
    first_number = second_number
    second_number = fib

print(total)
