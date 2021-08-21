# Importar Funciones Ahorcado

import funcionesahorcado as fa

palabra = fa.PalabraAleatoria()

vidasRestantes = fa.ElegirDificultad()


# Lista de letras usadas, creamos variables
letrasAcertadas = []
letrasFalladas = []

seguirJuando = True
while seguirJuando:

    #Mostrar la palabra con huecos en el usuario
    palabraConvertida = fa.ConvertirPalabraEnHuecos(palabra,letrasAcertadas)
    print ('------------------')
    print ('Palabra adivinar es:', palabraConvertida)
    print ('Vidas Restantes:', vidasRestantes)
    print ('Letras falladas:', letrasFalladas)
    print ('------------------')

    # Esperamos que el usuario introduzca una letra
    letraIntroducida = input ('Introduce una letra:')

    # Opción 1 la letra ya fue ingresada
    if (letraIntroducida in letrasAcertadas or letraIntroducida in letrasFalladas): 
        print ('------------------')
        print('Esta lista ya ha sido utilizada, elige otra letra')
        continue
    else:
        if (letraIntroducida in palabra):
            print ('------------------')
            print('La letra', letraIntroducida, 'esta en la palabra')
            letrasAcertadas.append(letraIntroducida)
        else:
        # Comprobar si la letra esta o no en nuestra palabra
            print ('La letra', letraIntroducida, 'no esta en la palabra')
            vidasRestantes -=1
            letrasFalladas.append(letraIntroducida)
# Comprobar si el usuario ha perdido todas las vidas
    if (vidasRestantes == 0):
        print ('------------------')
        print('Has perdido todas las vidas la palabra es', palabra)
        seguirJuando = fa.EvaluarSeguirJugando()

    else:
        # Si tiene vidas seguir jugando
        # Comprobar si la palabra esta completa
        palabraCompleta = fa.PalabraCompleta(palabra,letrasAcertadas)
        
        # Si la palabra esta completa el usuario ha ganado
        if (palabraCompleta == True):
            print ('Todas las letras han sido acertadas')
            seguirJuando = fa.EvaluarSeguirJugando()
    
    if (vidasRestantes == 0 and seguirJuando or (fa.PalabraCompleta(palabra,letrasAcertadas) and seguirJuando)): 
        letrasFalladas = []
        letrasAcertadas = []
        vidasRestantes = fa.ElegirDificultad()
        palabra = fa.PalabraAleatoria()

print ('------------------')
print ('Gracias por jugar, ¡Hasta la próxima!')
print ('------------------')