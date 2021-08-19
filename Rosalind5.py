lines=[]
with open('Bio.txt') as f:
	lines = f.readlines()

i=0
for line in lines: 
	i+=1
	if i % 2 == 0:
		print i, ":", line

f.close()
