# Programa que calcule el promedio de N cantidad de notas de un alumno
# Si el promedio es mayor a 70 entonces queda aprobado
# El programa debe arrojar la nota final, decir si esta aprobado e indicar nombre del alumno
# Ademas preguntar si desea capturar otro alumno

cantidad = 0
nombreAlumno = input('Ingresa el nombre del alumno :')
listaC = []
sumaLista = 0
promedio = 0


validacionR = True
while (validacionR):

    cantidad = int (input ('¿Cuantas calificaciones vas a promediar? :'))

    for i in range (1,cantidad+1): # (1,cantidad ingresada + 1) --> serian el rango
                                   

        # cuando se indica dos elementos en range el primer elemento pasa a indicar el incio
        # es decir va a empezar en 1

        # el segundo valor indica que cuando ingrese por ejemplo cantidad = 8
        # colocaria cantidad + 1 para que el bucle culmine cuando llegue a 8

        # va empezar 1,2,3,4,5,6,7,8

        # si colocara range(5,8)
        # va a empezar en 5, 6, 7 --> culmina en 
        
        print ('Ingresa la', i,'calificacion:')
        calificacion = int (input(''))
        listaC.append(calificacion) # notas ingresadas en lista
        cantidadN = len (listaC) #cantidad de notas ingresadas
        
    sumaLista = 0
    for i in listaC:
        sumaLista += i # --> i + sumaLista
    
    promedio = sumaLista / cantidadN

    if (promedio >= 70):
        print ('El alumno:', nombreAlumno, 'tiene promedio de', promedio, 'y esta APROBAD0')
    if (promedio <= 70):
        print ('El alumno:', nombreAlumno, 'tiene promedio de', promedio, 'y esta REPROBAD0')
    

    while (True):
        respuesta = input ('¿Desea ingresar otro alumno? S / N :')
        if  (respuesta == 'S'):
            validacionR = True
            break
        elif(respuesta == 'N'):
            validacionR = False
            break
        else:
            print('Ingrese opción valida')
