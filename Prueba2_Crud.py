import sqlite3
import bcrypt

DB_NAME = "Glados.db"

conexion = sqlite3.connect(DB_NAME)
cursorBD = conexion.cursor()

cursorBD.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contraseña TEXT NOT NULL
)
""")
conexion.commit()
conexion.close()

print("Base de datos Glados creada correctamente")

######################################################################################
def encender_glados():
        conexion = sqlite3.connect(DB_NAME)
        cursorBD = conexion.cursor()
        return conexion, cursorBD

while True:
    print("\n--- MENÚ ---")
    print("1- Crear usuario")
    print("2- Mostrar usuarios")
    print("3- Modificar usuario")
    print("4- Eliminar usuario")
    print('5- Iniciar sesión')
    print("6- Salir")

    try:
        opcion = int(input('Seleccione una opción: '))
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.")
        continue

    match opcion:
        case 1:
            conexion, cursorBD = encender_glados()

            nombre = input('Escriba su nombre de usuario: ').lower()

            cursorBD.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
            if cursorBD.fetchone() is not None:
                print("El nombre de usuario ya existe. Elija otro.")
                conexion.close()
                continue

            contraseña = input('ingrese su contraseña (debe ser de 8 carácteres como mínimo): ')

            while len(contraseña) < 8:
                contraseña = input('ingrese una contraseña válida (debe ser de 8 carácteres como mínimo): ')

            contraseña = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursorBD.execute("INSERT INTO usuarios (nombre, contraseña) VALUES (?, ?)", (nombre, contraseña))
            conexion.commit()
            conexion.close()

            print(f'Usuario {nombre} fué agregado con éxito!!!')

        case 2:
                conexion, cursorBD = encender_glados()

                cursorBD.execute("SELECT id, nombre FROM usuarios")
                usuarios = cursorBD.fetchall()

                if len(usuarios) == 0:
                    print("No hay usuarios registrados.")
                else:
                    print("\nUsuarios registrados:")
                    for id_usuario, nombre in usuarios:
                        print(f"{id_usuario} - {nombre}")

                conexion.close()

        case 3:
            
            conexion, cursorBD = encender_glados()

            cursorBD.execute("SELECT id, nombre FROM usuarios")
            usuarios = cursorBD.fetchall()

            if len(usuarios) == 0:
                print("No hay usuarios para modificar.")
                conexion.close()
                continue
            else:
                for id_usuario, nombre in usuarios:
                    print(f"{id_usuario} - {nombre}")

            try:
                id_modificar = int(input("Ingrese el ID del usuario a modificar: "))
            except ValueError:
                print("ID no válido. Por favor, ingrese un número.")
                conexion.close()
                continue

            nuevo_nombre = input("Nuevo nombre: ").lower()
            nueva_contraseña = input("Nueva contraseña: ")

            while len(nueva_contraseña) < 8:
                nueva_contraseña = input("Ingrese contraseña válida (mínimo 8): ")
            nueva_contraseña = bcrypt.hashpw(nueva_contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            cursorBD.execute("""
            UPDATE usuarios
            SET nombre = ?, contraseña = ?
            WHERE id = ?
            """, (nuevo_nombre, nueva_contraseña, id_modificar))

            conexion.commit()

            if cursorBD.rowcount == 0:
                print("ID no encontrado.")
            else:
                print("Usuario modificado correctamente.")

            conexion.close()


        case 4:
            conexion, cursorBD = encender_glados()
            
            cursorBD.execute("SELECT id, nombre FROM usuarios")
            usuarios = cursorBD.fetchall()
            if len(usuarios) == 0:
                print("No hay usuarios para eliminar.")
                conexion.close()
                continue
            else:
                print("\nUsuarios:")
                for id_usuario, nombre in usuarios:
                    print(f"{id_usuario} - {nombre}")

            try:
                id_eliminar = int(input("Ingrese el ID del usuario a eliminar: "))
            except ValueError:
                print("ID no válido. Por favor, ingrese un número.")
                conexion.close()
                continue

            cursorBD.execute("DELETE FROM usuarios WHERE id = ?", (id_eliminar,))
            conexion.commit()

            if cursorBD.rowcount == 0:
                print("ID no encontrado.")
                conexion.close()
                continue
            else:
                print("Usuario eliminado correctamente.")

            conexion.close()
        
        case 5:
            conexion, cursorBD = encender_glados()

            if 'intentos_fallidos' not in globals():
                intentos_fallidos = {}

            nombre_usuario = input("Ingrese su nombre de usuario: ").lower()
            contraseña_usuario = input("Ingrese su contraseña: ")

            if nombre_usuario not in intentos_fallidos:
                intentos_fallidos[nombre_usuario] = 0

            if intentos_fallidos[nombre_usuario] >= 3:
                print("Demasiados intentos fallidos. Intente nuevamente más tarde.")
                conexion.close()
                continue

            cursorBD.execute("SELECT contraseña FROM usuarios WHERE nombre = ?", (nombre_usuario,))
            resultado = cursorBD.fetchone()
            if resultado is None:
                print("Usuario no encontrado.")
            else:
                contraseña_almacenada = resultado[0]
                if bcrypt.checkpw(contraseña_usuario.encode('utf-8'), contraseña_almacenada.encode('utf-8')):
                    print("Inicio de sesión exitoso.")
                    intentos_fallidos[nombre_usuario] = 0
                else:
                    print("Contraseña incorrecta.")
                    intentos_fallidos[nombre_usuario] += 1
            conexion.close()
        case 6:
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")