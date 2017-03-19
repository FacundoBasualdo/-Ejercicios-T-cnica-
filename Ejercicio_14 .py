contador = 0
frase = raw_input("Ingresar Una Frase: ")
for letra in frase:

    if (letra == "a"):
        contador = contador + 1

    elif (letra == "e"):
            contador = contador + 1

    elif (letra == "i"):
            contador = contador + 1

    elif (letra == "o"):
            contador = contador + 1

    elif (letra == "u"):
        contador = contador + 1

print ("")
print ("HAY " + str(contador) + " VOCALES")
