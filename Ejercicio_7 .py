print ("")
print ("  CALCULADORA   ")
print ("")

calculadora_encendida = True
while (calculadora_encendida):
    print ("-------------------------------------------------------------------")
    print (" Si Finalizo De Operar Escriba (salir) En La Siguiente Interaccion")
    print ("-------------------------------------------------------------------")
    print ("")
    operacion = raw_input(" Ingrese (1 Para Sumar), (2 Para Restar), (3 Para Dividir), (4 Para Multiplicar), (Escriba (salir) Para Cuando Termine): ")


    if (operacion == ("salir")):
        calculadora_encendida = False


    elif (operacion == "1"):
        print ("")
        valor1 = raw_input(" Ingrese Un Valor: ")
        print ("")
        valor2 = raw_input(" Ingrese Un Segundo Valor: ")
        print ("")
        resultado_sumar = float(valor1) + float(valor2)
        print ("          El Resultado Es " + str(resultado_sumar))
        print ("")


    elif (operacion == "2"):
        print ("")
        valor1 = raw_input(" Ingrese Un Valor: ")
        print ("")
        valor2 = raw_input(" Ingrese Un Segundo Valor: ")
        print ("")
        resultado_restar = float(valor1) - float(valor2)
        print ("          El Resultado Es " + str(resultado_restar))
        print ("")


    elif (operacion == "3"):
        print ("")
        valor1 = raw_input(" Ingrese Un Valor: ")
        print ("")
        valor2 = raw_input(" Ingrese Un Segundo Valor: ")
        print ("")
        resultado_dividir = float(valor1) / float(valor2)
        print ("          El Resultado Es " + str(resultado_dividir))
        print ("")


    elif (operacion == "4"):
        print ("")
        valor1 = raw_input(" Ingrese Un Valor: ")
        print ("")
        valor2 = raw_input(" Ingrese Un Segundo Valor: ")
        print ("")
        resultado_multiplicar = float(valor1) * float(valor2)
        print ("          El Resultado Es " + str(resultado_multiplicar))
        print ("")

    else:
        print (" Opcion Incorrecta, Vuelvalo A Intentar")
