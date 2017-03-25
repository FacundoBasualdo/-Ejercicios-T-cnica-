
# lista_numeros = []
# contar = 0
# sumar = 0
# funcionando = True
# while (funcionando):
#    lista_numeros.append(raw_input("Ingresar Numero: "))
#    for numero in lista_numeros:
#        sumar = sumar + int(numero)
#        contar = contar + 1
#        if (contar == 15):          #### Con el 15 me deja pedir los 5 numeros, pero si pongo el 5 solo me deja 3. Por que?
#            promedio = int(sumar) / 5     #### Y en al dividir me pone cualquier numero, en la prueba que hice antes
#            print (promedio)                     puse 5 veces el 10 y como resultado me da 30. No se porque
#            funcionando = False


print ("")
print (" Debe Ingresar Numeros Para Mostrar El Promedio De Ellos.")
print ("")


lista_numeros = []
print ("Ingresa (salir) Al Terminar. ")

numeros_ingresar = True
while (numeros_ingresar):
    lista_numeros.append(raw_input("--> numeros: "))
    for caracter in lista_numeros:
        if (caracter == "salir"):
            lista_numeros.remove("salir")
            numeros_ingresar = False


sumar = 0
for numero in lista_numeros:
    sumar = sumar + int(numero)

divisor = 0
for numero in lista_numeros:
    divisor += 1

promedio = sumar / divisor

print ("")
print ("El Promedio Es De: " + str(promedio))
