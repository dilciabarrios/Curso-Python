# Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a 
# $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en
# compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al 
# cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el 
# descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si 
# es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y 
# ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el 
# programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.

import random

cantidadCompra = int (input ('Indique la cantidad de compra realizada: '))
descuento = 0
totalPagar =0 

lista = [ ["Bola Blanca", 'Sin descuento'],["Bola Amarilla", 10], ["Bola Roja", 20],["Bola Azul", 25],
     ["Bola Verde", 50],]
     
print ("{:<20} {:<50}".format('COLOR','DESCUENTO'))

for v in lista:
    color,  descuento = v
    print ("{:<20} {:<50}".format( color, descuento))

if (cantidadCompra >100):
    nroAleatorio =  random.randint(0,5)
    if (nroAleatorio == 0 and nroAleatorio == 1):
        color = 'Bola Amarilla'
        descuento = 10
        montoDescuento = cantidadCompra * 0.10
        totalPagar = cantidadCompra - montoDescuento
    elif (nroAleatorio == 2):
        color = 'Bola Roja'
        descuento = 20
        montoDescuento = cantidadCompra * 0.20
        totalPagar = cantidadCompra - montoDescuento
    elif (nroAleatorio == 3):
        color = 'Bola Azul'
        descuento = 25
        montoDescuento = cantidadCompra * 0.25
        totalPagar = cantidadCompra - montoDescuento
    elif (nroAleatorio == 4):
        color = 'Bola Verde'
        descuento = 50
        montoDescuento = cantidadCompra * 0.50
        totalPagar = cantidadCompra - montoDescuento
    elif (nroAleatorio == 5):
        color = 'Bola Blanca'
        print ('Sin Descuento')
    else:
        print('')

print ('Aleatoriamente obtuvo la', color)
print ('Felicidades obtuvo un', descuento, 'por ciento de descuento')
print ('Nuevo total a pagar es:', totalPagar)

