import sys

#N = 2**15
N = 2**1000

sum = 0
while N > 0:
	sum += N%10
	N //= 10

print('ANS : {}'.format(sum))
