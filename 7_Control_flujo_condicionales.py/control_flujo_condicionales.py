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

if (miEdad <=6 ):
    print('Entra gratis, usted no paga ya que es niño')
elif(miEdad >6 and miEdad<=21):
    preguntaBono = input ('¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):')
    if (preguntaBono == 's' in preguntaBono):
        print ('El precio de su entrada sin descuento es de $ 9 con el descuento son $ 8.1')
    else: 
        print ('El precio de su entrada es de $ 9')
elif(miEdad >21 and miEdad<=66):
    preguntaBono = input ('¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):')
    if (preguntaBono == 's' in preguntaBono):
        print ('El precio de su entrada sin descuento es de $ 14 con el descuento son $ 12.6')
    else: 
        print ('El precio de su entrada es de $ 14')
elif(miEdad >=67):
    preguntaBono = input ('¡De acuerdo! ¿Tiene usted el bono de descuento del 10% para este mes? (s/n):')
    if (preguntaBono == 's' in preguntaBono):
        print ('El precio de su entrada sin descuento es de $ 6 con el descuento son $ 5.4')
    else: 
        print ('El precio de su entrada es de $ 14')


