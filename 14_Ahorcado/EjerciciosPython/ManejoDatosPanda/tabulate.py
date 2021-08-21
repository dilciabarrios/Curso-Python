lista = [ ["Bola Blanca", 'Sin descuento'],["Bola Amarilla", 10], ["Bola Roja", 20],["Bola Azul", 25],
     ["Bola Verde", 50],]
     
print ("{:<20} {:<30}".format('COLOR','DESCUENTO'))

for v in lista:
    color,  descuento = v
    print ("{:<20} {:<30}".format( color, descuento))




