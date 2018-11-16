fifthpowers = []
testnum = 2
while testnum < 1000000.0:
	temp = 0.0
	for digit in str(testnum):
		temp += int(digit)**5
	if temp == testnum:
		fifthpowers.append(temp)
	testnum += 1
print sum(fifthpowers)
