# Contains functions used to solve problems from projecteuler.net

import math

def is_palindrome(n):
# Takes a string and returns True if it is a palindrome and false if not
	palindrome = n.find(n[::-1])
	if palindrome == -1:
		return False
	elif palindrome == 0:
            return True

def is_prime(n):
# If n is a prime number return True else return False
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

def gen_triangle(x):
# Returns the xth triangle number
    triangle = (x*(x+1))/2
    return triangle

def count_divisors(x):
# Returns the number of divisors for x
    count = 0
    square = math.sqrt(x)
    for y in range(1,int(square)):
        if x % y == 0:
            count += 1
    count = count *2
    if square * square != x:
        return count
    else:
        return count +1

def is_even(x):
# Returns True if x is even. Else returns False
    if x % 2 == 0:
        return True
    else:
        return False

def is_odd(x):
# Returns False if x is even. Else returns True
    if x % 2 == 0:
        return False
    else:
        return True

def create_collatz_sequence(x):
# Generate collatz sequence for x
    collatz_sequence = [x]
    while x != 1:
        if is_even(x):
            x = x/2
        else:
            x = ((3*x)+1)
        collatz_sequence.append(x)
    return collatz_sequence

def add_digits(n):
# Takes a number n and returns the sum of the digits of that number
# Ex 32768 3+2+7+6+8=26
    sum = 0

    for x in str(n):
        sum += int(x)

    return sum
