lines=[]
with open('Bio.txt') as f:
	lines = f.readlines()

i=0
for line in lines: 
	i+=1
	if i % 2 == 0:
		print i, ":", line

f.close()

#file=open('Bio.txt')
#linea=0
#for line in file
	#if linea % 2 == 0:
		#print line

#close('Bio.txt')
