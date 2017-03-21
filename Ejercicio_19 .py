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
        print ("")

        dic_contactos = {
            "nombre": raw_input("Ingresar El Nombre: "),
            "telefono": raw_input("Ingresar El Telefono: ")
        }

        lista_datos.append(dic_contactos)


    elif (opcion == "2"):
        print ("")
        for datos in lista_datos:
            print (dic_contactos["nombre"] + " , " + dic_contactos["telefono"])
            print ("")


    elif (opcion == "3"):
        while_encendido = False
    else:
        print ("Opcion Incorrecta")
        print ("")
