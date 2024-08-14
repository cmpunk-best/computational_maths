# Gets the lcm of 2 numbers
# Not efficient at all , better use dictionary, but who cares this is easy
from eulidgcf import gcd
def lcm(a, b):
	return (a * b ) / gcd(a, b) 

a = int(input("a:"))
b = int(input("b:"))
print(lcm(a, b))