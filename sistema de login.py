def espacio (a):
    for i in range (a):             #Esta funcion hace lineas de espacios
        print ("")

espacio(10)
print ("=====*PRUEBA SISTEMA DE LOGIN*=====")
print ("")


n1 = input("ingrese un nombre para su cuenta: ")
n2 = input("ingrese una contraseña: ")


espacio (10)


print ("=====*SISTEMA DE LOGIN*=====")
print ("")



print("hola, ingrese su usuario")
n3 = input("usuario: ")

if n3==n1:
    print("usuario correcto")
else:
    print("usuario incorrecto, ingreselo de vuelta: ")
    while n3 != n1:
        n3 = input("usuario: ")
espacio(1)
print("USUARIO CORRECTO")

espacio (3)


print("ingrese su contraseña: ")
n4 = input("contraseña: ")

if n4 == n2:
    print("contraseña correcta")
else:
    print("contraseña incorrecta, ingresela de nuevo: ")
    while n4 != n2:
        n4 = input("contraseña: ")
espacio(1)

print("CONTRASEÑA CORRECTA")

espacio(2)


print("*Bienvenido de nuevo*: ",n3 )

espacio(1)