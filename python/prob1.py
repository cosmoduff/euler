#!/usr/bin/env python
#Find the sum of all the multiples of 3 or 5 below 1000

divis = []

for n in range(1,1000,1):
    if (n%3==0) or (n%5==0):
        divis.append(n)

print(sum(divis))
