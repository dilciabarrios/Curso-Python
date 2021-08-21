#Objetivo: dividir las diferentes operaciones en funciones:
#Ademas, añadir:
#Una comprobacion que nos diga si el numero par o impar
#Una comprobacion que nos diga si el numero es primo o no

def ComprobarSiEsPar (numero):
    if (numero % 2 == 0):
        return True
    else:
        return False

def ComprobarMultiplos (numero):
    multiplos = []
    for num in range (1,6):
        numresultado = num*numero 
        multiplos.append(numresultado)
    print ('- Los multiplos son:', multiplos) 
    return multiplos
    

def ComprobarCuadrado (numero):
    cuadrado = numero**2
    print ('- Su número al cuadrado es:', cuadrado)

def ComprobarCubo (numero):
    cubo = numero**3
    print ('- Su número al cubo es:', cubo)

def ComprobarMultiplicado (numero):
    multiplicado = numero*100
    print ('- Su número multiplicado por 100 es:', multiplicado)

def ComprobarPrimo (numero):
    if (numero % 1 == 0 and numero % numero == 0  and numero % 2 != 0 and numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0):
        print('- El número', numero, 'es primo')
    elif (numero == 2 and numero == 3 and numero == 5 and numero ==7):
        print('- El número', numero, 'es primo')
    else:
        print ('- El número', numero, 'no es primo')

miNum = input ('Introduce un número:')
miNum = int (miNum)
resultado = ComprobarSiEsPar(miNum)
resultado1 = ComprobarPrimo(miNum)


if (resultado):
    print('- El número', miNum, 'es par ')
else:
    print('- El número', miNum, 'es impar ')


miMultiplos = ComprobarMultiplos(miNum)
alCuadrado = ComprobarCuadrado(miNum)
alCubo = ComprobarCubo (miNum)
multiplicado = ComprobarMultiplicado(miNum)
primos = ComprobarPrimo (miNum)
