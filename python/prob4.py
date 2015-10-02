#!/usr/bin/env python
#Find the largest palindrome made from the product of two 3-digit numbers.

product = 0
palindrome = 0

def isPalindrome(n):
	palindrome = n.find(n[::-1])
	if palindrome == -1:
		return False
	elif palindrome == 0:
		return True

for n in range(999,100,-1):
	for x in range(100,999,1):
		product = n * x
		if isPalindrome(str(product)) == True:
			if product > palindrome:
				palindrome = product

print(palindrome)
