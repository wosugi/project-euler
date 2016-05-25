import sys

#N = 10
N = 100

sum1 = N*(N+1)        //2
sum2 = N*(N+1)*(2*N+1)//6

ans = sum1*sum1-sum2
print('ANS : {}'.format(ans))
