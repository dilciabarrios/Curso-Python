#SINTAXIS PARA DEFINIR FUNCION
#def nombreDeMiFuncion(parametro1, parametro2...)
#codigo a ejecutar por la funcion
#return valorDeRetorno


def CalcularValorAlCuadrado(numero):
    numeroCuadrado = numero * numero
    return numeroCuadrado


print ('Hola amigos, inicio del programa:')
miNumero = input ('Introduce un numero:')
miNumero = int (miNumero)

miNumeroAlCuadrado = CalcularValorAlCuadrado (miNumero)
print ('Mi numero al cuadrado es:' , miNumeroAlCuadrado)

def ImprimePalomitas ():
    print ('Palomitas')

ImprimePalomitas()
