# Crear una funcion que nos diga si un numero es par o no

def ComprobarSiEsPar (numero):
    if (numero % 2 == 0 ):
        return True
    else:
        return False

miNum = input ('Introduce un numero:')
miNum = int (miNum)
resultado = ComprobarSiEsPar(miNum)

if (resultado):
    print('El numero', miNum, 'es par porque comprobarSiEsPar retorno', resultado)
else:
    print('El numero', miNum, 'es impar porque comprobarSiEsPar retorno', resultado)