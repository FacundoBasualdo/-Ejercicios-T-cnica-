def contar_lista(lista_contada):
    contar = 0
    for caracteres in lista_contada:
        contar += 1
    return (contar)



def invertir_lista(lista):

    ultimo = contar_lista(lista) - 1
    primero = 0
    guardar_ultimo = ultimo
    while (guardar_ultimo > primero):
        guardar_primero = lista[primero]
        lista[primero] = lista[guardar_ultimo]
        lista[guardar_ultimo] = guardar_primero
        primero += 1
        guardar_ultimo = ultimo - primero
    return (lista)



lista_a_invertir = []
agregar_a_lista = True

while(agregar_a_lista):
    print("")
    lista_a_invertir.append(raw_input("Ingrese Numeros, Palabras, Lo Que Quiera, Al Finalizar Ponga (salir1): "))

    for caracter in lista_a_invertir:
        if (caracter == "salir1"):
            lista_a_invertir.remove("salir1")
            agregar_a_lista = False


print ("")
print (invertir_lista(lista_a_invertir))
