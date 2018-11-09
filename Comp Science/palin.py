palin = []
numb = 0
palinnumb = 0
for x in range(999,100,-1):
	for y in range(999,100,-1):
		numb = x * y
		palinnumb = str(numb)[::-1]
		if str(palinnumb) == str(numb):
			palin.append(numb)
print max(palin)