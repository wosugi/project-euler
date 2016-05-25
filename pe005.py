import sys

#N = 10
N = 20

# Euclidean algorithm 
def gcd(a,b):
	while b != 0:
		t = a%b
		a = b
		b = t
	return a

def lcm(a,b):
	return a*b//gcd(a,b)

ans = 1
for i in range(2,N+1):
	ans = lcm(ans,i)

print('ANS : {}'.format(ans))
