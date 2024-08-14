#Finding gcd using Euclidean method
"""
How did he come up with this?
May be he just needed some way to just not apply brain, and 
do dumb calculations. Becoz for large numbers finding factors is 
cumbersome....Maybe
"""
import time
def euclidgcf(a, b):
	rem = a % b
	if (rem == 0):
		return b  
	return euclidgcf(b, rem)
def gcd(a, b):
	min_ab = min(a, b)
	max_ab = max(a, b)
	return euclidgcf(max_ab, min_ab)
a = int(input("Enter a number: "))
b = int(input("Enter another number:"))
t0 = time.time()
print(gcd(a, b))
t1 = time.time()
print("timetaken",t1 - t0)

