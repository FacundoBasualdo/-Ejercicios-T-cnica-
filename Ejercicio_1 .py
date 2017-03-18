print ("")
usuario_creado = raw_input("Crea Un Nombre De Usuario: ")
contrasena_creado = raw_input("Crea Una Contrasena: ")
print ("")
print ("Usted A Creado Un Usuario Y Contrasena Escribala Correctamaente Para Ingresar Al Sistema")
print ("")

usuario_correcto = True
while (usuario_correcto):
    usuario = raw_input("Ingrese Su Usuario Correctamente: ")
    if (usuario_creado == usuario):
        usuario_correcto = False
    else:
        print ("")
        print ("Usuario Incorrecto")
contrasena_correcta = True

while (contrasena_correcta):
    contrasena = raw_input("Ingrese Su contrasena Correctamente: ")
    if (contrasena_creado == contrasena):
        print ("")
        print ("A Ingresado Al Sistema Correctamente")
        contrasena_correcta = False
    else:
        print ("")
        print ("Contrasena Incorrecta")
