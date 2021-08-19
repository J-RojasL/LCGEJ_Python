a=input("Ingrese el numero de inicio:\t")
b=input("Ingrese el numero en el que desea terminar:\t")

c=0
for x in range(a,b):
	if x % 2 == 1:
		c+=x
print "\nLa suma de todos los enteros en ese rango es \n", c
