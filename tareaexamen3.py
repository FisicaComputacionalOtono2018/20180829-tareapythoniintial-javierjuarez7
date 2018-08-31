#Javier Juarez Jimenez
#Programa que calcula el producto vectorial de dos vectores en el espacio

import math
A1=input('Escribe la componente en x del vector A: ')
A2=input('Escribe la componente en y del vector A: ')
A3=input('Escribe la componente en z del vector A: ')
B1=input('Escribe la componente en x del vector B: ')
B2=input('Escribe la componente en y del vector B: ')
B3=input('Escribe la componente en z del vector B: ')

x=A2*B3-A3*B2
y=A3*B1-A1*B3
z=A1*B2-A2*B1

print 'El producto vectorial da como resultado: ',x ,'i +',y ,'j +' ,z ,'k'

