import sys

N = 4000000

sum = 0
n2,n1 = 1,1
while n1 < N: # Fibonacci numbers
	n0 = n1+n2
	if n0%2 == 0: sum += n0
	n2 = n1
	n1 = n0

print('ANS : {}'.format(sum))
