from time import sleep
i = 0
while i <= (5*60):
	if i % 60 != 0:
		print i
	else:
		print "%d minute" % (i/60)
	i = i+1
	sleep(1)