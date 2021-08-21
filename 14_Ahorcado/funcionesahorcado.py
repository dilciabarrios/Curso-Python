import random

def ElegirDificultad():

    vidasRestantes = 0 

    while (True):

        # El usuario debe elegir una dificultad

        dificultad = input ('Escoge un nivel de dificultad: F (FACILIL), M (MEDIO), D (DIFICIL) :')
        if ( dificultad == 'F'):
            print ('Nivel seleccionado es: FACIL') 
            vidasRestantes = 9 
            break
        elif (dificultad == 'M'):
            print ('Nivel seleccionado es: MEDIO')
            vidasRestantes = 6
            break
        elif (dificultad == 'D'):
            vidasRestantes = 3
            print ('Nivel seleccionado es: DIFICIL')
            break
        else:
            print ('Selecciona una opción válida: F (FACILIL), M (MEDIO), D (DIFICIL) ')

    return vidasRestantes

def ConvertirPalabraEnHuecos(palabra, letrasAcertadas):

    palabraConvertida = ''

    for letra in palabra:
        if (letra in letrasAcertadas):
            palabraConvertida += letra + ' '
        else:
            palabraConvertida += '* '

    return palabraConvertida

def PalabraCompleta(palabra, letrasAcertadas):
    for letra in palabra:
        if (letra in letrasAcertadas):
            continue
        else:
            # Si la palabra no esta completa seguir jugando
            return False

    return True

def EvaluarSeguirJugando ():
    print ('------------------')
    JugarOtraVez = input ('¿Quieres jugar otra partida? S/N : ')
    seguirJuando = False
    
    while (True):
            if (JugarOtraVez == 'S'):
                seguirJuando = True
                break
            elif (JugarOtraVez == 'N'):
                seguirJuando = False
                break
            else:
                print ('Entrada Inválida, Seleccione S/N')
    return seguirJuando


def PalabraAleatoria():
    ficheroPalabras = open('mispalabras.txt', 'r')
 
    listaPalabras = []
    for linea in ficheroPalabras:
        linea = linea.replace('\n','')
        listaPalabras.append(linea)  
    ficheroPalabras.close()

    # [0,1,2,3] -> longitud 4
    # (0,longitud -1) -> 3

    posicionDeLaLista = random.randint(0,len(listaPalabras)-1)
    return listaPalabras[posicionDeLaLista]

