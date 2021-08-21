# Trabajar con ficheros en Python:
# open(nombreDelFichero, modoDeApertura)
# r -> Read - Leer
# w -> Write - Escribir
# a -> Append - Añadir
# r+ -> Read+ - Leer y escribir

miArchivo = open('mifichero.txt', 'r')


# Leo una segunda linea
segundaLineaLeida = miArchivo.readline()
print(segundaLineaLeida)

terceraLineaLeida = miArchivo.readline()
print(terceraLineaLeida)


miArchivo.close()


