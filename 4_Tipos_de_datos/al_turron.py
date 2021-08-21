#Objetivos de este al turron 
#A partir de 4 datos en variables, obtener el precio de un deposito de gasolina
#Imprimir el precio para que aparezca en una factura 
#Componerlo todo en una unica string
#---------Factura-----------
#Combustible: DIESEL
#Precio: 1.395 $/1
#Litros: 44.59
#Surtidor: 17
#Importador total: 62.20 $

precio = '1.394394'
litros = 44.59
surtidor = 17.0
combustible = 'diesel'


#CONVERTIR STRING EN FLOAT

precio = float (precio) 
litros = float (litros)

#CONVERTIR EN MAYUSCULA
combustibleMayus = combustible.upper() 

#PARA SALTO DE LINEA
mensajeEncabezado = '---------Factura---------*'
mensajeEncabezado1 = '---------Factura--------- \n'
saltoFactura = (mensajeEncabezado.replace ('*','\n')) #salto de linea

#CONVERTIR EN ENTERO
surtidorInt = int(surtidor)

#CALCULO DE IMPORTE (MULTIPLICACION)
importe = precio * litros

#MENSAJE FINAL EN UNA SOLA LINEA
mensajeFactura = '%sEl precio por %.2f litros es de %.3f $/1, ubicado en surtidor: %d, el tipo de combustible es de: %s, Importe de: %f ' %(saltoFactura,litros,precio,surtidorInt,combustibleMayus, importe)
print (mensajeFactura)

#MENSAJE FINAL EN VARIAS LINEAS
linea1 = mensajeEncabezado1
linea12 = 'Combustible: %s \n' %(combustibleMayus)
linea2= 'Precio: %.3f \n'%(precio)
linea3= 'Litros: %.2f \n'%(litros)
linea4= 'Surtidor: %d \n'%(surtidorInt)
linea5= 'Importe: %f \n'%(importe)


facturaMensaje = mensajeEncabezado1 + linea12 + linea2 + linea3 + linea4 + linea5
print (facturaMensaje)
