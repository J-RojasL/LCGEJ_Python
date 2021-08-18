a = input("Ingrese la medida de uno de los catetos de su triangulo")
b = input("Ingrese la medida del otro cateto")

if a>1000:
	a= input("El cateto a debe tener un valor menor a 1000")

if b>1000:
	b= input("El cateto b debe tener un valor menor a 1000")

c2= a**2 + b**2

print "La medida de la hipotenusa al cuadrado es:", c2
