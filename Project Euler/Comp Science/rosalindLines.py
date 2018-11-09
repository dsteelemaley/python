doc = open('rosalind_ini5.txt', 'r')
length = str(doc)
newdoc = str()
for x in range(0,len(length),1):
	if x % 2 != 0:
		newdoc += doc.readline()
	else:
		doc.readline()
print newdoc
doc.close()