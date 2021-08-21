#IndexError: si intentamos acceder a una posicion de la lista o string que no existe

#miDiccionario = dict(Pedro= 7, Juan=19)
#try:
#    print(miDiccionario['Jose'])
#except KeyError:
#    print('ERROR- LA POSICION NO EXISTE')

miVariable = 20

try:
    print(miVariable)
except NameError:
    print('ERROR, TE COLASTE EL NOMBRE DE LA VARIABLE')