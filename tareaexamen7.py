#Javier Juarez Jimenez
#Algoritmo que calcula la velocidad de los corredores

m=float(1500)
t=float(60)
for i in range(1,1000):
        print 'Introduce el tiempo del corredor, primero minutos y luego segundos separados por un espacio. Si no quieres seguir escribiendo tiempo escribe 0 0:'
        mins, segs = raw_input().split()
        mins, segs = [float(mins), float(segs)]
        while not mins==0:
                while not segs==0:
                        tt = mins*t+segs
                        vel= m/tt
                        print 'El corredor tuvo un tiempo de' , mins , 'minutos y' , segs , 'segundos'
                        print 'La velocidad del corredor es de' , vel , 'metros por segundo'
                        break
                break
        if mins==0 and segs==0:
                break

