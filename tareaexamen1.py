#Javier Juarez Jimenez
#Programa que calcula el angulo entre dos vectores

import math
A1=input('Escribe la componente en x del vector A: ')
A2=input('Escribe la componente en y del vector A: ')
A3=input('Escribe la componente en z del vector A: ')
B1=input('Escribe la componente en x del vector B: ')
B2=input('Escribe la componente en y del vector B: ')
B3=input('Escribe la componente en z del vector B: ')

pp=A1*B1+A2*B2+A3*B3
pm=(math.sqrt(A1**2+A2**2+A3**2))*(math.sqrt(B1**2+B2**2+B3**2))
arad=float(math.acos(pp/pm))
ang=math.degrees(arad)
print 'El angulo entre los vectores es de' , ang, 'grados' 

