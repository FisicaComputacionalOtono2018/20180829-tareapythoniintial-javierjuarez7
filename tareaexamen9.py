#Javier Juarez Jimenez
#Programa que calcula la solucion de un sistema de ecuaciones de dos incognitas

print 'Escribe los valores de a, b y c en la primera ecuacion ax+by=c separados por espacios'
a, b, c = raw_input().split()
print 'Escribe los valores de d, e y f en la segunda ecuacion dx+ey=f separados por espacios'
d, e, f = raw_input().split()

a, b, c, d, e, f = [float(a), float(b), float(c), float(d), float(e), float(f)]
x=(c*e-b*f)/(a*e-b*d)
y=(a*f-c*d)/(a*e-b*d)
print 'El valor de x es' , x
print 'EL valor de y es' , y
