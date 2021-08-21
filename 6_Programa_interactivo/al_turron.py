#Dado un numero introducido por el usuario, tenemos que imprimir por pantalla

#Sus 5 primeros multiplos
#Su valor al cuadrado
#Su valor al cubo
#Su valor multiplicado por 100
#Ejemplo (vista de consola)
# >> Sus 5 primeros multiplos: 23.0 46.0 69.0 92.0 115.0
# >> Su valor al cuadrado y su cubo: 529.0 12167.0
# >> Su valor por 100: 2300.0


miNumero = input ('Introduce tu número para calcular:')
miNumero = float(miNumero)

#SUS PRIMEROS 5 MULTIPLOS
print('Sus primeros 5 multiplos:', miNumero, miNumero*2, miNumero*3, miNumero*4, miNumero*5)

#SU VALOR AL CUADRADO  Y AL CUBO
print('Su valor al cuadrado y al cubo :', miNumero**2, miNumero**3)

#SU VALOR MULTIPLICADO POR 100
print('Su valor multiplicado por 100:', miNumero*100)

