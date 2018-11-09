notprime = []
primes = [2]
for n in range(2,2000000):
	for x in primes:
		if n % x == 0:
			break
	else:
		primes.append(n)
print sum(primes)