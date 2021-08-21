#usuario = input('Introduce tu usuario:')
#contraseña = input ('Introduce tu contraseña:')

#if (usuario == 'Guille'):
#    if(contraseña == 'patatas'):
#        print('Bievenido Guillermo')
#    else:
#        print('Usuario o contraseña incorrectos')
#else:
#    print('Usuario o contraseña incorrectos')


#usuario = input('Introduce tu usuario:')
#contraseña = input ('Introduce tu contraseña:')

#if (usuario == 'Guille' and contraseña == 'patatas'):
#    print('Bievenido Guillermo')
#else:
#    print('Usuario o contraseña incorrectos')


#and - para que la condicion general se cumpla,todas las condiciones especificas tienen que ser verdaderas
#or - para que la condicion se cumpla, al menos una de las especificadas tiene que ser verdadera


condicionA = 5 > 3 
condicionB = 5 == 3

if (condicionA and condicionB):
    print('Todas las condiciones son verdaderas')

if (condicionA or condicionB):
    print ('Al menos una de las condiciones es verdadera')