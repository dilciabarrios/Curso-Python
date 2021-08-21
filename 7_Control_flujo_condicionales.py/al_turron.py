#Objetivo : decirle al usuario el precio que tendria que pagar por su entrada al museo
#las tarifas son:
#Niño (hasta 6 años): No paga
#Joven (hasta 21 años): 9$
#Adulto: 14$
#Jubilado (a partir de 67 años): 6$
#Además, hemos repartido unos descuentos en el ultimo mes del 10%. Si un usuario tiene un descuento y lo dice, tenemos que descontarle ese 10% del precio.
#Norma extra:
# - Si es niño, no preguntar si tiene descuento o no. Si es gratis es gratis.
# - Si tiene un descuento, mostrar precio con y sin descuento
# - Si no tiene descuento, mostrar unicamente el precio normal

#Ejemplo
# >>¡Hola! Bienvenido al Museo Python
# >>
# >> Si quiere saber el precio de su entrada, por favor indique su edad: 37
# >> ¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):s
# >>
# >> El precio de su entrada sin descuento es de 14.0$ con el descuento, son 12.6$


print ('¡Hola! Bienvenido al Museo Python')
miEdad = input('Si quiere saber el precio de su entrada, por favor indique su edad:')

miEdad= int(miEdad)

precio = 0

if (miEdad <=6):
    precio = 0
elif (miEdad >=6 and miEdad<=21):
    precio=9
elif(miEdad >=21 and miEdad<=66):
    precio=14
else: precio = 6



if (precio ==0):
    print ('No paga nada porque es un niño menor de 6 ¡Felicidades!')
elif (precio ==9):
    preguntaBono = input('¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):')
    if (preguntaBono == 's' in preguntaBono):
        calculoDescuento = precio*0.10
        descuento = precio - calculoDescuento
        print ('El precio de su entrada sin descuento es de %d con el descuento, son %.2f' %(precio,descuento))
    else: print ('El precio de su entrada es de %d'%(precio))
elif (precio ==14):
    preguntaBono = input('¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):')
    if (preguntaBono == 's' in preguntaBono):
        calculoDescuento = precio*0.10
        descuento = precio - calculoDescuento
        print ('El precio de su entrada sin descuento es de %d con el descuento, son %.2f' %(precio,descuento))
    else: print ('El precio de su entrada es de %d'%(precio))
elif (precio ==6):
    preguntaBono = input('¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):')
    if (preguntaBono == 's' in preguntaBono):
        calculoDescuento = precio*0.10
        descuento = precio - calculoDescuento
        print ('El precio de su entrada sin descuento es de %d con el descuento, son %.2f' %(precio,descuento))
    else: print ('El precio de su entrada es de %d' %(precio))




