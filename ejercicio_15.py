lista_numeros = []
encender = True
print ("")
print ("Al Finalizar De Ingresar Escriba (salir)")
print ("")
while(encender):
    lista_numeros.append(raw_input("Escribir Numero: "))
    print ("")
    for caracter in lista_numeros:
        if (caracter == "salir"):
            lista_numeros.remove("salir")
            encender = False

mayor = 0
for numero in lista_numeros:
    if (int(numero) > int(mayor)):
        mayor = numero

print ("")
print ("El Numero Mayor Es " + mayor)
