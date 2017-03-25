print ("")
bancos = raw_input("Ingrese La Cantidad De Bancos: ")
print ("")
alumnos = raw_input("Ingrese La Cantidad De Alumnos: ")
print ("")

if (alumnos > bancos):
    bancos_faltantes = int(alumnos) - int(bancos)
    print ("Faltan " + str(bancos_faltantes) + " Bancos")
else:
    bancos_sobrantes = int(bancos) - int(alumnos)
    print ("Sobran " + str(bancos_sobrantes) + " Bancos")
