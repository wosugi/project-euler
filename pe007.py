import sys

#N = 6-1
N = 10001-1

# Sieve of Eratosthenes
def gen_primes(n=105000):
	primes = []
	flags = [True]*(n+1)
	flags[0] = False
	flags[1] = False
	for i in range(2,n+1):
		if flags[i] == False:
			continue
		primes.append(i)
		for j in range(i+i,n+1,i):
			flags[j] = False
	return primes

primes = gen_primes()
print('ANS : {}'.format(primes[N]))
