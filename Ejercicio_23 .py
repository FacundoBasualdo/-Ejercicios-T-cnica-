def cortar (cortante):

    lista_ingresados = []
    while_ingresar = True
    while (while_ingresar):
        lista_ingresados.append(raw_input("Ingresar: "))
        print ("")
        for caracter in lista_ingresados:
            if (caracter == cortante):
                lista_ingresados.remove(caracter)
                while_ingresar = False
    return lista_ingresados

print ("")
cortante = raw_input("Elija Uncaracter Para Cortar: ")
print ("")
funcion = cortar(cortante)
print ("")
print (funcion)
print ("")
