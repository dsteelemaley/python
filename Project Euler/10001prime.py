notprime = []
primes = [2]
testnumb = 3
while len(primes) < 10001:
	for x in primes:
		if testnumb % x == 0:
			notprime.append(testnumb)
	if testnumb not in notprime:
		primes.append(testnumb)
	testnumb += 2
print primes
