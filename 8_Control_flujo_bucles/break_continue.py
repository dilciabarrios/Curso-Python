# Break y continue
# Son dos palabras clave(keywords) que nos dan un control extra sobre bucles o loops

nombreUsuarios = ['Juan', 'Martha', 'Miguel', 'Elisa', 'Claudia','Jorge', 'Ana']

# Break: Interrumpe el loop y pasa a la siguiente instruccion fuera del loop
# Continue : Interrumple el loop y vuelve al inicio del mismo para siguiente vuelta

for nombre in nombreUsuarios:
    print('Mi usuario es', nombre)
    if( nombre == 'Elisa'):
        continue
    print ('Ejecuta esto mienstra usuario no sea Elisa')
print('Esto se ejecuta fuera del loop')