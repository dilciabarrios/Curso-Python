# formatear un string es introducir datos dentro de ellos.

combustible = 'de Gasolina'
precioPorLitro = 1.329
duracionPrecio = 5


#combinamos varios elementos en una string

mensaje = 'El precio por litro %s en los próximos %d dias es de %.2f $/1' %(combustible, duracionPrecio, precioPorLitro)

# limitar decimales %.2f redondear

print (mensaje)


# los strings se formatean con tanto %s
# los enteros se formatean con tanto %d
# los floats se formatean con tanto %f


#utilizar funcion format()
mensajedeprueba = 'Mi entero: {0:d}'.format(duracionPrecio)
print(mensajedeprueba)

mensajedeprueba2 = 'Mi float: {0:f} Mi float con 2 decimales {0:.2f}'.format(precioPorLitro)
print(mensajedeprueba2)

ultimaprueba = 'Mi numero 1:{} y mi numero 2:{}' .format(precioPorLitro, duracionPrecio)
print (ultimaprueba)

