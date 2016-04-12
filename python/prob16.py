# What is th sum of the digits of the number 2^1000?

import math

num = 2**1000

num_str = str(num)
solution = 0

for x in num_str:
   solution += int(x)

print(solution)
