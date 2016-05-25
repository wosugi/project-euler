import sys

N = 1000

def search(n):
	for a in range(1,N):
		for b in range(a+1,N):
			if N**2+2*a*b == 2*N*(a+b):
				return a,b,N-a-b

a,b,c = search(N)
print('(a,b,c) = ({},{},{})'.format(a,b,c))
print('ANS : {}'.format(a*b*c))
