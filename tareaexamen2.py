#Javier Juarez Jimenez
#Programa que calcula los angulos con respecto a los ejes de un vector en el espacio

import math 

x=input('Escribe la componente x del vector: ')
y=input('Escribe la componente y del vector: ')
z=input('Escribe la componente z del vector: ')

a=math.degrees(math.acos(x/(math.sqrt(x**2+y**2+z**2))))
b=math.degrees(math.acos(y/(math.sqrt(x**2+y**2+z**2))))
c=math.degrees(math.acos(z/(math.sqrt(x**2+y**2+z**2))))

print'El angulo con respecto al eje x es de', a, 'grados'
print'El angulo con respecto al eje y es de', b, 'grados'
print'El angulo con respecto al eje z es de', c, 'grados'
