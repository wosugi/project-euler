import sys

N = 600851475143

ans = 0
n = N
while 1 < n:
	print('n = {}'.format(n))
	for i in range(2,n+1):
		if n%i == 0:
			n //= i
			break
	print('A prime factor : {}'.format(i))
	ans = i

print('ANS : {}'.format(ans))
