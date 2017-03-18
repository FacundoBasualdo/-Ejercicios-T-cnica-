print ("")
monto = raw_input(" Escriba Total A Pagar: $")
print ("")
encendido = True
while (encendido):
    metodo_pago = raw_input(" Ponga --> 1 <-- Si Paga Al Contado, --> 2 <-- Para No: ")
    print ("")
    if (metodo_pago == "1"):
        descuento = int(monto) / 10
        total_descuento = int(monto) - int(descuento)
        print (" El Total Es De $" + str(total_descuento))
        encendido = False
    elif (metodo_pago == "2"):
        print (" $" + monto)
        encendido = False
    else:
        print ("Opcion Incorrecta, Elija Una De Las Opciones")
        print ("")
