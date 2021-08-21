# Importando modulos: tenemos 3 opciones.
# Opción 1: Importat todo un módulo

import random

# Llamar a funciones de random: nombreDelModulo.nombreDeLaFuncion
# Llama un número aleatorio
miNumeroRandom = random.randint(1,100)
print (miNumeroRandom) 

# Opción 2: Importar el módulo pero con otro nombre: para que sea más sencillo llamarlo
import random as r 

# Llamar a funciones:
miNumeroRandom = r.randint(1,100)
print (miNumeroRandom)

# Opción 3: Importar únicamente
from random import randint, random
# Llamar a la función es más sencillo
miUltimoNuevRandom = randint (1,100)
print (miNumeroRandom)
