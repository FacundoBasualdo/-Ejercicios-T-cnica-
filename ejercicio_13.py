
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



lista_numeros = []
numero1 = raw_input("Escriba un numero: ")
numero2 = raw_input("Escriba un numero: ")
numero3 = raw_input("Escriba un numero: ")
numero5 = raw_input("Escriba un numero: ")
numero4 = raw_input("Escriba un numero: ")
lista_numeros.append(numero1)
lista_numeros.append(numero2)
lista_numeros.append(numero3)
lista_numeros.append(numero4)
lista_numeros.append(numero5)
numeros_sumados = float(numero1) + float(numero2) + float(numero3) + float(numero4) + float(numero5)
promedio_numeros = numeros_sumados / 5
print promedio_numeros
