import sys

palinds = []
for a in range(100,1000):
	for b in range(100,1000):
		n = a*b
		digits = str(n)
		if digits == digits[::-1]:
			palinds.append(n)
			#print('{} = {} x {}'.format(digits,a,b))

ans = max(palinds)
print('ANS : {}'.format(ans))
