# 3 pasos a seguir para importar un módulo propio:
# 1 - Tener el módulo localizado
# 2 - Hacer un import sys
# 3 - Añadir al path nuestro módulo

import sys

if ('/home/vauxoo/Escritorio/ModulosPython' not in sys.path):
    sys.path.append('/home/vauxoo/Escritorio/ModulosPython')

import funcionesmatematicas


miNumero = 28
miCuadrado = funcionesmatematicas.ComprobarCuadrado(miNumero)
print(miCuadrado)
