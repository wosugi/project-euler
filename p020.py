import sys
import math

#N = math.factorial(10)
N = math.factorial(100)

sum = 0
while N > 0:
	sum += N%10
	N //= 10

print('ANS : {}'.format(sum))
