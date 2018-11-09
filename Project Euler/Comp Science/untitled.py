sumsqr = 0
sqrsum = 0
sums = 0
for x in range(1,101):
	sumsqr += x**2
for x in range(1,101):
	sums += x
sqrsum = sums**2

print sumsqr-sqrsum
print sqrsum-sumsqr