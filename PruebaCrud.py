usuarios = []

while True:
    print("\n--- MENÚ ---")
    print("1- Crear usuario")
    print("2- Mostrar usuarios")
    print("3- Modificar usuario")
    print("4- Eliminar usuario")
    print("5- Salir")
    
    opcion = int(input('Seleccione una opción: '))

    match opcion:
        case 1:
            nombre = input('Escriba su nombre de usuario: ').lower()
            contraseña = input('ingrese su contraseña (debe ser de 8 carácteres como mínimo): ')

            while len(contraseña) < 8:
                contraseña = input('ingrese una contraseña válida (debe ser de 8 carácteres como mínimo): ')

            usuarios.append((nombre, contraseña))
            print(f'Usuario {nombre} fué agregado con éxito!!!')

        case 2:
            if len(usuarios) == 0:
                print("No hay usuarios registrados.")

            else:
                print("\nUsuarios registrados:")
                for i, (nombre, _) in enumerate(usuarios):
                    print(f"{i} - {nombre}")

        case 3:
            if len(usuarios) == 0:
                print("No hay usuarios para modificar.")

            else:
                for i, (nombre, _) in enumerate(usuarios):
                    print(f"{i} - {nombre}")
                indice = int(input("Ingrese el índice del usuario a modificar: "))

            if 0 <= indice < len(usuarios):
                nuevo_nombre = input("Nuevo nombre: ")
                nueva_contraseña = input("Nueva contraseña: ")
                usuarios[indice] = (nuevo_nombre, nueva_contraseña)
                print("Usuario modificado correctamente.")

            else:
                print("Índice inválido.")

        case 4:
            if len(usuarios) == 0:
                print("No hay usuarios para eliminar.")

            else:
                for i, (nombre, _) in enumerate(usuarios):
                    print(f"{i} - {nombre}")
                indice = int(input("Ingrese el índice del usuario a eliminar: "))

            if 0 <= indice < len(usuarios):
                eliminado = usuarios.pop(indice)
                print(f"Usuario {eliminado[0]} eliminado correctamente.")

            else:
                print("Índice inválido.")
    
        case 5:
            print("Saliendo del programa...")
            break