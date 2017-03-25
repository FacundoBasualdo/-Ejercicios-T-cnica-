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

numero_menor = lista_numeros[0]
for numero in lista_numeros:
    if (int(numero) < int(numero_menor)):
        numero_menor = numero

print ("")
print ("El Numero Menor Es " + numero_menor)
