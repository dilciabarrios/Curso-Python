print('Bienvenido al sistema de almacenamiento de usuarios.')

usuarios = ['Juan','Marta','Miguel','Elisa','Claudia','Jorge','Ana','Pedro']
while(True):
    print('''---
    ¿Qué operación deseas realizar?
    1 - Ver una lista de usuarios
    2 - Añadir un usuario
    3 - Eliminar un usuario
    X - Salir del programa''')

    opcionElegida = input('Introduce la opción: ')
    print('---')
    if(opcionElegida == '1'):
        print('Lista de usuarios')
        for usuario in usuarios:
            print(usuario)
    elif(opcionElegida == '2'):
        nuevoUsuario = input('Introduce el nombre del nuevo usuario: ')
        usuarios.append(nuevoUsuario)
        print(nuevoUsuario, 'añadido')
    elif(opcionElegida == '3'):
        usuarioAEliminar = input('¿Qué usuario quieres eliminar?:')
        usuarios.remove(usuarioAEliminar)
        print(usuarioAEliminar, 'eliminado')
    elif(opcionElegida == 'X'):
        break
    else:
        print('Entrada inválida.')