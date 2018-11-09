from random import randint
routes = 0
direction = 0
right = 0
down = 0
path = 0

while right < 20 and down < 20:
	direction = randint(0,1)
	if direction == 0 and right < 20:
		right += 1
	if direction == 1 and down < 20:
		down += 1

if right >= 20 and down >= 20:
		path +=1
print path