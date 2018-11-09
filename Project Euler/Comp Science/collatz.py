from time import time
termtemp = 1
term = {"1":"1"}
s = time()
for number in range(2,1000000):
	lol = number
	while number != 1:
		if number % 2 == 0:
			number = number/2
			termtemp += 1
		else:
			number = (number*3)+1
			termtemp += 1
	term[str(termtemp)] = str(lol)
	termtemp = 1
print term[max(term)]