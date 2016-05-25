import sys

#N = 10
N = 2000000

# Sieve of Eratosthenes
def gen_primes(n):
	primes = []
	flags = [True]*(n)
	flags[0] = False
	flags[1] = False
	for i in range(2,n):
		if flags[i] == False:
			continue
		primes.append(i)
		for j in range(i+i,n,i):
			flags[j] = False
	return primes

primes = gen_primes(N)
print('ANS : {}'.format(sum(primes)))
