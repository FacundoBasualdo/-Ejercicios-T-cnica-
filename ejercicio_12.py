print ("")
lista_numeros = []
pedir = True
contar = 0

while(pedir):
    lista_numeros.append(raw_input("Ingrese Un Numero: "))
    print ("")
    for numero in lista_numeros:
        contar += 1
        if (contar ==  50):
            print lista_numeros
            pedir = False
