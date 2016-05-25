import sys
import math

# use Pascal's triangle

#N = 2
N = 20

def nCr(n,r):
	fact = math.factorial
	return fact(n)//fact(r)//fact(n-r)

ans = nCr(2*N,N)
print('ANS : {}'.format(ans))
