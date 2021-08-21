# Construye un programa que al recibir los datos de
# Peso, Altura y Genero de N personas de un estado y pais
# Obtenga el promedio del Peso, Alura de la poblacion femenina y masculina
 
 
sumaPesoF = 0
sumaPesoM = 0
promedioPesoF = 0
promedioPesoM = 0
promedioAlturaF=0
promedioAlturaM=0
sumaAlturaF = 0
sumaAlturaM = 0
generosFemeninos = []
generosMasculinos = []
cantidad = 0

validacionR = True
while  (validacionR):

    cantidad = int (input ('¿Cual sera la cantidad de personas a ingresar ?: '))

    for i in range (cantidad):
        genero = input ('Indique genero F (Femenino) M (Masculino):')
        peso = int (input ('Ingresa peso: '))
        altura = float (input ('Ingrese altura: '))

        if  (genero == 'F'):
            generosFemeninos.append(genero)
            cantidadFemeninos = len (generosFemeninos)

            sumaPesoF += peso
            promedioPesoF = sumaPesoF/cantidadFemeninos

            sumaAlturaF += altura
            promedioAlturaF = sumaAlturaF / cantidadFemeninos

        elif (genero == 'M'):
            generosMasculinos.append(genero)
            cantidadMasculinos = len (generosMasculinos)

            sumaPesoM += peso
            promedioPesoM = sumaPesoM/cantidadMasculinos
            
            sumaAlturaM += altura
            promedioAlturaM = sumaAlturaM /cantidadMasculinos

        else:
            print('Ingrese una cantidad válida')
            break

    respuesta = input('¿De que genero desea obtener información F (Femenino) / M (Masculino) / A (Ambos): ?')

    if (respuesta == 'F'):
        print ('La suma de los pesos femeninos es :', sumaPesoF)
        print ('Su promedio es :', promedioPesoF)

        print ('La suma de las alturas femeninas es : % .2f'% (sumaAlturaF))
        print ('Su promedio es : % .2f'% (promedioAlturaF))
    elif (respuesta == 'M'):
        print ('La suma de los pesos masculinos es :', sumaPesoM)
        print ('Su promedio es :', promedioPesoM)

        print ('La suma de las alturas masculinas es :', sumaAlturaM)
        print ('Su promedio es :', promedioAlturaM)
    elif (respuesta == 'A'):
        print ('FEMENINO')
        print ('La suma de los pesos femeninos es :', sumaPesoF)
        print ('Su promedio es :', promedioPesoF)

        print ('La suma de las alturas femeninas es : % .2f'% (sumaAlturaF))
        print ('Su promedio es : % .2f'% (promedioAlturaF))
        print ('--------------------------------------------------')
        print ('MASCULINO')
        print ('La suma de los pesos masculinos es :', sumaPesoM)
        print ('Su promedio es :', promedioPesoM)

        print ('La suma de las alturas masculinas es :', sumaAlturaM)
        print ('Su promedio es : %.2f' % (promedioAlturaM))
    else:
        print ('Ingrese una opción válida: F (Femenino) / M (Masculino) / A (Ambos)')


    

    while (True):

        respuesta = input ('¿Desea ingresar mas datos?: S / N :')
        
        if (respuesta == 'S'):
            validacionR = True
            break
            
        elif(respuesta == 'N'):
            validacionR= False
            print ('Culminamos')
            break
        else:
            print('Ingrese una opción válida:')


