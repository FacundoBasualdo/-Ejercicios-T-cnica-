print ("")
print (" Debe Ingresar Sus 5 Notas Para Saber Que Promedio Tiene.")
print ("")


nota_1 = True
while (nota_1):
    nota1 = raw_input("--> Primer Nota: ")
    if (int(nota1) <= 10):
        print ("")
        nota_1 = False
    else:
        print ("")
        print (" No Hay Nota Mayor A 10, Vuelva A Intentarlo.")
        print ("")


nota_2 = True
while (nota_2):
    nota2 = raw_input("--> Segunda Nota: ")
    if (int(nota2) <= 10):
        print ("")
        nota_2 = False
    else:
        print ("")
        print (" No Hay Nota Mayor A 10, Vuelva A Intentarlo.")
        print ("")


nota_3 = True
while (nota_3):
    nota3 = raw_input("--> Tercer Nota: ")
    if (int(nota3) <= 10):
        print ("")
        nota_3 = False
    else:
        print ("")
        print (" No Hay Nota Mayor A 10, Vuelva A Intentarlo.")
        print ("")


nota_4 = True
while (nota_4):
    nota4 = raw_input("--> Cuarta Nota: ")
    if (int(nota4) <= 10):
        print ("")
        nota_4 = False
    else:
        print ("")
        print ("")
        print (" No Hay Nota Mayor A 10, Vuelva A Intentarlo.")


nota_5 = True
while (nota_5):
    nota5 = raw_input("--> Quinta Nota: ")
    if (int(nota5) <= 10):
        print ("")
        nota_5 = False
    else:
        print ("")
        print (" No Hay Nota Mayor A 10, Vuelva A Intentarlo.")
        print ("")


suma_notas = int(nota1) + int(nota2) + int(nota3) + int(nota4) + int(nota5)
promedio = int(suma_notas) / 5
if (int(promedio) >= 7):
    print ("")
    print ("----------")
    print (" APROBADO")
    print ("----------")
else:
    print ("")
    print ("-------------")
    print (" DESAPROBADO")
    print ("-------------")
