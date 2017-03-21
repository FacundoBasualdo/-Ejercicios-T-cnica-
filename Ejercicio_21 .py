def buscar_reemplazar(lista, buscador, reemplazante):

    lista_meter = []
    for caracter in lista:
        lista_meter.append(caracter)
        if (caracter == buscador):
            lista_meter.remove(caracter)
            lista_meter.append(reemplazante)

    return lista_meter


lista_creada = [1, 2, 3, 4, 5, 6]

lista_con_cambios = buscar_reemplazar(lista_creada, 2, 9)
print ("")
print (lista_con_cambios)
