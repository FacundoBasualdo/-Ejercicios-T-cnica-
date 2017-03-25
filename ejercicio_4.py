print ("")
usuario = raw_input(" Escriba Nombre De Usuario: ")
print ("")



if(usuario == "admin"):
    crear_contrasena = raw_input("Crea La Contrasena: ")
    admin = True
    while(admin):
        contrasena = raw_input("Escriba La Contrasena: ")
        if(contrasena == crear_contrasena):
            print ("")
            print (" BIENVENIDO ADMINISTRADOR")
            admin = False
        else:
            print ("")
            print (" Contrasena Incorrecta")
            print ("")



elif(usuario == "operador"):
    crear_contrasena = raw_input(" Crea La Contrasena: ")
    operador = True
    while(operador):
        contrasena = raw_input("Escriba La Contrasena: ")
        if(contrasena == crear_contrasena):
            print ("")
            print (" BIENVENIDO OPERADOR")
            operador = False
        else:
            print ("")
            print (" Contrasena Incorrecta")
            print ("")


elif(usuario != "admin"):
    print ("")
    print (" USUARIO DESCONOCIDO")



elif(usuario != "operador"):
    print ("")
    print (" USUARIO DESCONOCIDO")
