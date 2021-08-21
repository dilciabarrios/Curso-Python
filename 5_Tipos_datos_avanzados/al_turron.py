#Tenemos una lista con nombres de ciudades 
ciudadesDeEspaña = ['Granada','Cordoba','Santiago de Compostela','Paris','Malagá', 'Barcelona']
otrasCiudades = ['Toledo','Sevilla','Cadiz','Berlin','Alicante']


#Tareas
# 1- Quitar de la listas las ciudades que no pertezcan a España (Berlin y Paris)
# 2- Unir ambas listas en una unica
# 3- Añadir Madrid, la capital, en la primera posicion de la lista, porque no esta
# 4- Añadir otras ciudades a tu eleccion (Por Ejemplo: Mallorca, Santander y Burgos)
# 5- Imprimir la siguiente frase por pantalla
# >> Mi lista de ciudades tiene {numero de ciudades aquí} ciudades: [Contenido de la lista]


# 1-ELIMINANDO CIUDADES
del ciudadesDeEspaña [3]
print('Eliminando Ciudad de Paris \n',ciudadesDeEspaña)
del otrasCiudades [3]
print('Eliminando Ciudad de Berlin \n',otrasCiudades)

# 2- UNIR AMBAS LISTAS
ciudadesDeEspaña.extend(otrasCiudades)
print('Uniendo ambas listas el resultado es:')
print (ciudadesDeEspaña)

# 3- AÑADIR MADRID EN LA PRIMERA POSICION
ciudadesDeEspaña[0]= 'Madrid'
print('El resultando añandiendo Madrid es:\n',ciudadesDeEspaña)

# 4- AÑADIR OTRAS CIUDADES
ciudadesDeEspaña.append('Mallorca')
ciudadesDeEspaña1 = ciudadesDeEspaña
ciudadesDeEspaña1.append('Santander')
ciudadesDeEspaña2 = ciudadesDeEspaña1
ciudadesDeEspaña2.append('Burgos')
print ('Añandiendo nuevas ciudades:\n',ciudadesDeEspaña2)

# 5-AÑADIENDO INFORMACION DE LA LISTA

numeroDeElementos =len(ciudadesDeEspaña2)
print ('>> Mi lista de ciudades tiene %d ciudades:\n>> Las Ciudades Son:\n %s' %(numeroDeElementos,ciudadesDeEspaña2))

