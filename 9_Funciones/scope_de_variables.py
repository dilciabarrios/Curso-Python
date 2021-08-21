# una variable declarada dentro de una funcion se conoce como varible local
# una variable declarada fuera de la funcion se conoce como varible global


mensaje1 = 'Soy una variable global'

def miFuncion():
    print ('Estoy dentro de mi funcion')
    #crear variable local
    mensaje2 = 'Soy la variable local'

    #Acceso a variable local:
    print (mensaje2)

    #Acceso a variable global:
    print (mensaje1)

#Llamar a mi funcion
miFuncion()

#Hacer cosas fuera de la funcion:
print ('Estoy fuera de la funcion')

#Acceso a la variable global:
print (mensaje1)


