#Find the sum of all primes below two million.

import threading  
import math

class SummingPrimes(threading.Thread):
	def __init__(self, low, high):
		super(SummingPrimes, self).__init__()
		self.low = low
		self.high = high
		self.total = 0

	def isPrime(self, x):
		if x < 2:
			return False
		if x in (2,3):
			return True
		if x % 2 == 0 or x % 3 ==0:
			return False
		max_divisor = int(x ** 0.5)
		divisor = 5
		while divisor <= max_divisor:
			if x % divisor == 0 or x % (divisor + 2) == 0:
				return False
			divisor += 6
		return True
		""" My orig code
		if x < 2:
			return False
		if x == 2 or x ==3:
			return True
		if x % 2 == 0 or x % 3 == 0:
			return False
		for n in range(2, math.ceil(math.sqrt(x+1))): 
			if x % n == 0:
				return False
		return True"""

	def run(self):
		for i in range (self.low, self.high):
			if self.isPrime(i):
				self.total += i

thread1 = SummingPrimes(1, 750000)
thread2 = SummingPrimes(750000, 1500000)
thread3 = SummingPrimes(1500000, 1750000)
thread4 = SummingPrimes(1750000, 2000000)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

result = thread1.total + thread2.total + thread3.total + thread4.total

print(result)
