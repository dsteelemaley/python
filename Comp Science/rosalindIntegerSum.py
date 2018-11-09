a = int(raw_input('Int:'))
b = int(raw_input('Int:'))
c = 0

for e in range(a,b+1):
	if e % 2 != 0:
		c += e
print c