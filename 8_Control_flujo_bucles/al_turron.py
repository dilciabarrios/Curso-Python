#OBJETIVOS: GENERAR LA SERIE FIBONACCI, IMPRIMIENDO EL NUMERO DE ELEMENTOS
#Que el usuario quiera
#Serie de fibonacci: 0,1,2,3,4,5,8,13,21,34,55.... El siguiente número es 
#La suma de los anteriores 
#Cosas a cumplir:
#- Pedir al usuario que introduzca un número de elementos
#Pedirle que introduzca un número 
#- Imprimir los X primeros terminos de la serie, siendo X el numero introducido por el usuario
#- El número de los elementos tiene que ser mayor que 1

while(True):
    numeroElementos = input ('Introduce el numero de elementos a calcular, minimo 2:')
    try:
        #evalua que el numero de elemento para calcular fibonacci sea entero y luego mayor e igual a 2
        numeroElementos = int(numeroElementos)
        if (numeroElementos >=2 ):
            break
        #una vez verificado que sea entero y mayor e igual a 2 sale del bucle while
        else:
        #en caso de que no que no se cumplan la condicion de >=2 entonces emitir mensaje recordando
            print ('Por favor el nro de elementos el cual tiene que ser mayor o igual que 2')
            continue
        #continua el bucle while nuevamente
    except:
        #en caso de no cumplirse ninguno de los anteriores mandar mensaje de error con EXCEPT
        print ('Entrada no valida. Por favor introduce un numero')    

print ('Los primeros', numeroElementos, 'de la serie de fibonacci:')
num1= 0
num2= 1
#crear un contador para nuestro loop 
contador = 0

while (contador < numeroElementos):
    print(num1)
    #calcular el siguiente numero
    numeroSiguiente = num1 + num2
    #Actualizar los valores para la siguiente vuelta
    num1 = num2
    num2 = numeroSiguiente
    contador += 1

print ('-----FIN DEL PROGRAMA------')