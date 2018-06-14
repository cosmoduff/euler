#!/usr/bin/env python
#Find pythagorean triplet

for a in range(500,1,-1):
	for b in range(500,1,-1):
		for c in range(500,1,-1):
			if a + b + c == 1000 and (a*a) + (b*b) == (c*c):
				print(a*b*c)
				quit()
