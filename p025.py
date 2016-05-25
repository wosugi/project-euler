import sys

#N = 10**(3-1)
N = 10**(1000-1)

index = 2
n2,n1 = 1,1
while n1 < N: # Fibonacci numbers
	index += 1
	n0 = n1+n2
	n2 = n1
	n1 = n0

print('ANS : {}'.format(index))
