print ("")
print (" Debe Ingresar Sus Notas Para Saber Que Promedio Tiene.")
print ("")


lista_notas = []
print ("Ingresa (salir) Al Terminar. ")

nota_ingresar = True
while (nota_ingresar):
    lista_notas.append(raw_input("--> Nota: "))
    for caracter in lista_notas:
        if (caracter == "salir"):
            lista_notas.remove("salir")
            nota_ingresar = False

    for nota in lista_notas:
        if (int(nota) <= 10):
            print ("")
        else:
            lista_notas.remove(nota)
            print ("")
            print (" No Hay Nota Mayor A 10, Vuelva A Intentarlo.")
            print ("")


sumar = 0
for nota in lista_notas:
    sumar = sumar + int(nota)

divisor = 0
for nota in lista_notas:
    divisor += 1

promedio = sumar / divisor
if (int(promedio) >= 7):
    print ("Su Promedio Es De " + str(promedio) + ", Usted Esta: ")
    print ("")
    print ("----------")
    print (" APROBADO")
    print ("----------")
else:
    print ("Su Promedio Es De " + str(promedio) + ", Usted Esta: ")
    print ("")
    print ("-------------")
    print (" DESAPROBADO")
    print ("-------------")
