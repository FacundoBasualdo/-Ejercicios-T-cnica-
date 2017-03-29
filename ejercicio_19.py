lista_datos = []
while_encendido = True
while(while_encendido):
    print ("")
    print ("Ingresar (1) Para Cargar Nombre Y Telefono.")
    print ("")
    print ("Ingresar (2) Para Imprimir.")
    print ("")
    print ("Ingresar (3) Para Salir.")
    print ("")

    opcion = raw_input ("Igrese La Opcion: ")
    print ("")

    if (opcion == "1"):

        nombre = raw_input(" Escriba Su Nombre: ")
        print ("")
        telefono = raw_input(" Escriba Su Telefono: ")

        datos = {
            "nombre": nombre,
            "telefono": telefono
        }

        lista_datos.append(datos)


    elif (opcion == "2"):
        for datos in lista_datos:
            print ("")
            print "  Nombre: " + datos["nombre"] + ", " + "Telefono: " + datos["telefono"]
            print ("")



    elif (opcion == "3"):
        while_encendido = False
    else:
        print ("Opcion Incorrecta")
        print ("")
