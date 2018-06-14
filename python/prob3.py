#!/usr/bin/env python
#What is the largest prime factor of the number 600851475143?

num = 600851475143
prime = 0

def getprime(p):	#find prime number 
   for n in range(2,p):
       if p % n == 0:
          p = p / n
          print(n)

getprime(num)

# to do
# make it so that the program terminates
