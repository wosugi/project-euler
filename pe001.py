import sys

#N = 10-1
N = 1000-1

sum = lambda n: (n+1)*n//2

a =  3*sum(N// 3)
b =  5*sum(N// 5)
c = 15*sum(N//15)

print('ANS : {}'.format(a+b-c))
