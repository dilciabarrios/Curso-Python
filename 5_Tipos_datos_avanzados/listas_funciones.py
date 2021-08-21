milista = ['a', 'b', 'c', 'd']
print (milista)


#Añadir elemento al final de la lista
milista.append('e')
print('Tras añadir:', milista)
 

#Insertar un elemento en una posicion de mi lista:
milista.insert(0,'x')
print('Tras añadir:', milista)

#Eliminar un elemento por su posicion
del milista[3]
print ('Tras eliminar:',milista)

#Combinar dos listas
miSegundaLista = ['a','f','g']
milista.extend(miSegundaLista)
print ('Tras Extender:', milista)

#Comprobar si un elemento existe en nuestra lista
print('Existe c en mi lista?')

resultado = 'c' in milista
print(resultado)

#Contar el numero de elementos que hay en mi lista
numeroDeElementos = len(milista)

print('Mi lista tiene %d elementos'%(numeroDeElementos))


#Eliminar un elemento concreto de mi lista

milista.remove('a')
print('Tras eliminar a:',milista)

milista.remove('z')