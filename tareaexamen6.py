#Javier Juarez Jimenez
#Programa que lee cuatro numeros e imprime el mayor de los cuatro

a=input('Escribe el primer numero: ')
b=input('Escribe el segundo numero: ')
c=input('Escribe el tercer numero: ')
d=input('Escribe el cuarto numero: ')

if a>b:
	if a>c:
		if a>d:
			print 'El numero mayor es ',a
if b>a:
	if b>c:
		if b>d:
			print 'El numero mayor es ',b
if c>a:
	if c>b:
		if c>d: 
			print 'El numero mayor es ',c
if d>a:
	if d>b:
		if d>c:
			print 'El numero mayor es ', d
