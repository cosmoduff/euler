#!/usr/bin/env python
#Find the largest palindrome made from the product of two 3-digit numbers.

import euler

product = 0
palindrome = 0

for n in range(999,100,-1):
	for x in range(100,999,1):
		product = n * x
		if euler.is_palindrome(str(product)) == True:
			if product > palindrome:
				palindrome = product

print(palindrome)
