#!/usr/bin/env python
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 tp 20?

number=2520

def remainder (n):
	remainder = 0
	for x in range(20,2,-1):
		if n%x == 0:
			continue
		else:
			return False
			break

while remainder(number) == False:
	number += 2520
	if remainder(number) != False:
		print(number)
		break
