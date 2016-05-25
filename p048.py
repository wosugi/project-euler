import sys

#N = 10
N = 1000

sum = sum([n**n for n in range(1,N+1)])
print(sum)

ans = sum%(10**10)
print('ANS : {}'.format(ans))
