dolar = 15.60
euro = 17.90
while_convertir = True
while(while_convertir):
    print ("")
    print ("----------------------------------------------")
    print (" Si Termino De Convertir Escriba (salir).")
    print ("----------------------------------------------")
    print ("")
    moneda_Ingresar = raw_input(" Ingrese Si Quiere Convertir A Pesos Con (euro) O (dolar): ")
    print ("")


    if (moneda_Ingresar == "salir"):
        while_convertir = False


    elif (moneda_Ingresar == "euro"):
        pesos_euros = raw_input ("Ingrese La Cantidad De (EUROS) Que Quiera Convertir A PESOS: ")
        print ("")
        resultado_euro = float(pesos_euros) * euro
        print ("--->La Cantidad Convertida Es De " + str(resultado_euro) + " PESOS")


    elif (moneda_Ingresar == "dolar"):
        pesos_dolares = raw_input ("Ingrese La Cantidad De (DOLARES) Que Quiera Convertir A PESOS: ")
        print ("")
        resultado_dolar = float(pesos_dolares) * dolar
        print ("--->La Cantidad Convertida Es De " + str(resultado_dolar) + " PESOS")
    else:
        print (" -<Elija (euro) o (dolar), SU OPCION ES INCORRECTA!>-")
