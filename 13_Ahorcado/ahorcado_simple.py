vidasRestantes = 0

palabra = 'PATATA'
letrasAcertadas = []
letrasFalladas = []

while(True):

    nivel = input ('Escoge un nivel de dificultad: F (FACILIL), M (MEDIO), D (DIFICIL) :')

    if (nivel == 'F'):
        print ('Nivel seleccionado es: FACIL') 
        vidasRestantes = 9
        break
    elif (nivel == 'M'):
        print ('Nivel seleccionado es: MEDIO')
        vidasRestantes = 6
        break
    elif (nivel == 'D'):
        print ('Nivel seleccionado es: DIFICIL')
        vvidasRestantes = 3
        break
    else:
        print ('Selecciona una opción válida')

# Mostrar la palabra con astericos

while (True):

    palabraConvertida = ''

    for letra in palabra:
        if (letra in letrasAcertadas):
            palabraConvertida += letra 
        else:
            palabraConvertida += '*'

    print ('Palabra a adivinar es: ', palabraConvertida)
    print ('Vidas Restantes:', vidasRestantes)
    print ('Letras Falladas: ', letrasFalladas)

    # Esperamos que el usuario introduzca una letra
    letraIntroducida = input ('Introduce una letra: ')


    if (letraIntroducida in letrasAcertadas or letraIntroducida in letrasFalladas):
        print ('Esta letra ya ha sido utilizada, por favor elegir otra letra')
        continue
    else:
        if (letraIntroducida in palabra):
            print('Letra introducida esta en la palabra')
            letrasAcertadas.append(letraIntroducida)
        else:
            print('La letra introducida', letraIntroducida, 'no esta en la palabra')
            vidasRestantes -= 1
            letrasFalladas.append(letraIntroducida)
    if (vidasRestantes ==0):
        print ('Has perdido todas las vidas')
        break
    else:
        palabraCompleta = False
        for letra in palabra:
            if (letra in letrasAcertadas):
                palabraCompleta = True
                continue
            else:
                palabraCompleta = False
                break
        if (palabraCompleta == True):

            print ('Todas las letras han sido acertadas')
            break