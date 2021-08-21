num1=input('Introduce el primer numero:')
num2=input('Introduce el segundo numero:')
#resultado =int(num1) / int(num2)

#print('El resultado de la division es:', resultado)
#print('-------FIN DEL PROGRAMA-------')

#Try -except para manejar errores
#try:
#    resultado =int(num1) / int(num2)
#    print('El resultado de la division es:', resultado)
#except:
#    print('Algo no ha ido como esperaba: ERROR')
#print('-------FIN DEL PROGRAMA-------')

try:
    resultado = int(num1)/int(num2)
    print('El resultado de la division es', resultado)
except ValueError: #Si uno de los valores no vale para la operacion - el programa un tipo de datos que 
    print('ERROR, Quizas uno de los valores no era un numero')
except ZeroDivisionError: #Division por cero
    print('ERROR,No se puede dividir entre 0')
except Exception as e: #Tratar cualquier otro error
    print('ERROR, eL siguiente error desconocido ha ocurrido')


