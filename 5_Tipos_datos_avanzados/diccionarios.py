#crear un diccionario con usuarios y sus datos
#diccionario = ('identificador': datoAsociado)

edadesUsuarios = {'Pedro' :32, 'Rosa' :51, 'Juan':23, 'Jose': 29  }
print ('¿Que edad tiene pedro?, Pedro Tiene:', edadesUsuarios['Pedro'])

#IMPORTANTE: NO PODEMOS TENER KEYS (IDENTIFICADORES)REPETIDOS

#FORMA ALTERNATIVA DE CREAR UN DICCIONARIO LA FUNCION DICT()

#dict(identificador = datoAsociado)

misOtrasEdadesUsuarios = dict (Sara = 31, Antonio = 19, Marta = 35, Lucia = 48)
print ('¿Que edad tiene Marta?, Marta tiene:', misOtrasEdadesUsuarios['Marta'])

#Cambiar un valor de algun usuario
edadesUsuarios['Rosa'] = 52
print(edadesUsuarios['Rosa'])

#Imprimir diccionario entero
print (edadesUsuarios)

#Añadir un valor nuevo: Referenciar un Key/identificador que no exite antes y darle valor
misOtrasEdadesUsuarios['Paco'] = 61
print(misOtrasEdadesUsuarios)

# Eliminar un valor del diccionario
print ('Lista antes', misOtrasEdadesUsuarios)
del misOtrasEdadesUsuarios ['Sara']

print ('Lista despues de eliminar a Sara:', misOtrasEdadesUsuarios)

#Funciones extra para un diccionario
print (edadesUsuarios)
edadesUsuarios.clear()
print (edadesUsuarios)

#Saber cuales son mis Keys/Identificadores
print('Los keys de misOtrasEdadesUsuarios son:', misOtrasEdadesUsuarios.keys())

#Saber cuales son mis valores en un diccionario - funcion values
print('Los Valores de misOtrasEdadesUsuarios son:', misOtrasEdadesUsuarios.values())

#Saber cuantos elementos tenemos en un diccionario len()

print('El numero de elementos de misOtrasEdadesUsuarios', len(misOtrasEdadesUsuarios))