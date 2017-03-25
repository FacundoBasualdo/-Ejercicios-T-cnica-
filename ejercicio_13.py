
print ("")
print (" Debe Ingresar 5 Numeros Para Mostrar El Promedio De Ellos.")
print ("")


lista_numeros = []
contar = 0
numeros_ingresar = True
while (numeros_ingresar):
    lista_numeros.append(raw_input("--> numeros: "))
    contar += 1
    if (contar == 5):
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
