# Requisitos:

# El usuario escoge el nivel de dificultad. F: 9 vidas, M: 6 Vidas, D: 3 Vidas
# Las palabras se lean desde un archivo de texto
# La palabra elegida por el programa tiene que mostrarse en forma de 'huecos' --> PATATA --> _ _ _ _ _
# El usuario siempre sabe cuántas vidas le quedan
# El usuario siempre sabe si ha introducido una letra repetida
# Esperamos que el usuario introduzca una letra
# Si el usuario acierta todas las letras, gana
# Si el usuario pierde todas las vidas, pierde la partida
# Tras ganar o perder, se ofrece el usuario si quiere jugar otra partida o salir del juego

# El programa elige una palabra aleatoria
# Pedir al usuario la dificultad en la que quiere jugar
# Mostrar la palabra con huecos al usuario
# Esperamos que el usuario introduzca una letra
# --- Opción 1: La letra ya esta usada 
# ---- Modificar al usuario que la letra ya ha sido usada, no restar vidas, volver a pedir una letra
# --- Opción 2: La letra no ha sido usada
# ---- Comprobar si la letra esta o no en nuestra palabra
# ------- Opción 1: La letra esta en la palabra : Acierto -> Rellenar huecos de la palabra, volver al incio
# ------- Opción 2: La letra no esta en la palabra: Error -> Quitar una vida, añadir a la lista de letras falladas
# Comprobar si el usuario ha perdido todas las vidas
# --- Si aun tiene vidas, seguir jugando
# --- Si no tiene vidas, finalizar el juego y pedir al usuario si quiere jugar otra vez o no
# Comprobar si palabra no esta completa, seguir jugando 
# Si la palabra está completa, el usuario ha ganado, preguntar si quiere jugar otra partid


from os import W_OK
import random
import re
from typing import List

# El usuario escoge el nivel de dificultad. F: 9 vidas, M: 6 Vidas, D: 3 Vidas

life_by_level = { 'F': 9, 'M': 6, 'D': 3,}

level = input ('Escoge un nivel de dificultad: F (FACILIL), M (MEDIO), D (DIFICIL) :')

if (level == 'F'):
    print ('Nivel seleccionado es: FACIL') 
elif (level == 'M'):
    print ('Nivel seleccionado es: MEDIO')
elif (level == 'D'):
    print ('Nivel seleccionado es: DIFICIL')
else:
    print ('Selecciona una opción válida')

life = life_by_level.get(level, 0)

# Las palabras se lean desde un archivo de texto
# Convierto en una lista mis palabras del archivo TXT

data = [] 

with open("palabras.txt") as fname:
    lines = fname.readlines()
    for line in lines:
        data.append(line.strip('\n'))

# La programa elige una palabra random

word = random.choice(data) 
cantidadLetras = len(word)
num_word = len (word)

word_unknown = '*' * num_word
print ('La palabra adivinar es: %s' % word_unknown)

# Letras falladas
failed = []
print ('Letras falladas:', failed)

# Pedir al usuario que introduzca una letra

while (life > 0 ):

    word_1 = input ('Introduce una letra :')
    print ('--------------------')

    # Verifica que si la letra se encuentra en la palabra y emitir mensaje si acerto

    resultado = word_1 in word
    if (resultado == True):
        print ('Acertaste la letra ', word_1, 'se encuentra en la palabra')
        print ('--------------------')
        #Indica cantidad de veces que se encuentra la letra introducida en la palabra
        recuento = word.count(word_1)
        #print ('Letras acertadas:', recuento)
        life = life
        print ('Te quedan vidas: %d' % life)
    elif (life == 0):
        break
    else:
        print ('No has acertado')
        life = life - 1 
        print ('Te quedan vidas: %d' % life)
        print ('--------------------')


    find = word_1
    indices = []

    # Ciclo for para indicar los indices donde se encuentra la letra introducida

    for llave, valor in list(enumerate(word)):
        if valor == find:
            indices.append(llave)

    for ind in indices:
        word_unknown[ind] 

    word_unknown_list = list (word_unknown)

    for ind in indices:
        word_unknown_list[ind] = find

    # Emitir mensaje de la letra en la posicion de la palabra

    word_unknown = '' ''.join(word_unknown_list)
    
    ast = '*' in word_unknown
    if (ast == True):
        print (word_unknown)
    else:
        print('Juego finalizado')
        break

