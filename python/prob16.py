# What is th sum of the digits of the number 2^1000?

num = 2**1000

def add_digits(n):
# Takes a number n and returns the sum of the digits of that number
# Ex 32768 3+2+7+6+8=26
    result = sum(list(map(int, str(n))))
    return result 

print(add_digits(num))
