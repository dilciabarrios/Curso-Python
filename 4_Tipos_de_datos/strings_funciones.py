miString = 'Hola me llamo Guillermo'
print ('Mi string inicial', miString)


#poner una frase en mayuscula - upper

miStringMayus = miString.upper()
print ('String Mayus:', miStringMayus)

#Poner en minuscula - lower
print ('String minus:', miString.lower())
print ('Esto no modifica la string original:', miString)

#funcion replace - reemplaza caracteres de nuestro string
print ('Reemplazamos las o por las i:', miString.replace('o', 'i'))
print ('Este no modifica la string original:', miString)

#reemplazamos palabras enteras
print ('Reemplazo Guillermo por Hernandez:', miString.replace('Guillermo', 'Hernandez'))

#Reemplazamos las primeras 2 o por i:
print ('Reemplazamos las dos primeras o por i', miString.replace ('o','i',2))

#Pasar una frase de una de linea a multiples lineas
print(miString.replace(' ','\n'))