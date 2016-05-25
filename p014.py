import sys

# naive algorithm --- taking tens of seconds

#N = 10
N = 1000000

def count_collatz(n):
	if n == 1: return 1
	n = n//2 if n%2 == 0 else 3*n+1
	return 1+count_collatz(n)

steps = [-1]*(N+1)
for n in range(1,N+1):
	steps[n] = count_collatz(n)
	#if n%10000 == 0:
	#	print('{:7d} : {:4d}'.format(n,steps[n]))

ans = steps.index(max(steps))
print('ANS : {}'.format(ans))
