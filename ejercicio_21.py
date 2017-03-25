def buscar_reemplazar(lista, buscador, reemplazante):

    lista_reemplazante = []
    for caracter in lista:
        if (caracter == buscador):
            lista_reemplazante.append(reemplazante)
        else:
            lista_reemplazante.append(caracter)
    return lista_reemplazante


    return lista

lista = []
crear_lista = True
while (crear_lista):
    print ("")
    lista.append(raw_input("Ingrese Una Lista Con Cualquier Tipo De Datos. Al Finalizar Escribir (salir1): "))
    for dato in lista:
        if (dato == "salir1"):
            lista.remove("salir1")
            crear_lista = False

print ("")
print (lista)
print ("")
buscador = raw_input("Ingrese Un Dato Que Desee Cambiar De Su Lista: ")
print ("")
reemplazante = raw_input("Ingrese El Dato Que Quiere Cambiar Por El Anterior: ")

print ("")
print ("")
print (buscar_reemplazar(lista, buscador, reemplazante))
print ("")
print ("")
