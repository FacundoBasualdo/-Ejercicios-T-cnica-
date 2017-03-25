dolar = 15.60
euro = 17.90
while_convertir = True
while(while_convertir):
    print ("")
    print ("----------------------------------------------")
    print (" Si Termino De Convertir Escriba -->salir<--.")
    print ("----------------------------------------------")
    print ("")
    moneda_a_convertir = raw_input(" Ingrese Si Quiere Convertir A (euro) O (dolar): ")
    print ("")


    if (moneda_a_convertir == "salir"):
            while_convertir = False


    elif (moneda_a_convertir == "euro"):
        pesos = raw_input ("Ingrese Cuantos (Pesos) Quiere Convertir: ")
        print ("")
        resultado_euro = float(pesos) / euro
        print ("--->La Cantidad Convertida Es De " + str(resultado_euro) + " EUROS")


    elif (moneda_a_convertir == "dolar"):
        pesos = raw_input ("Ingrese Cuantos (Pesos) Quiere Convertir: ")
        print ("")
        resultado_dolar = float(pesos) / dolar
        print ("--->La Cantidad Convertida Es De " + str(resultado_dolar) + " DOLARES")

    else:
        print (" -<Elija (euro) o (dolar), SU OPCION ES INCORRECTA!>-")
