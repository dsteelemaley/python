number = 600851475143
factor = 2
primes = []

while factor < number:
	if number % factor == 0:
		number = number/factor
		primes.append(factor)
	else:
		factor += 1
print str(number)