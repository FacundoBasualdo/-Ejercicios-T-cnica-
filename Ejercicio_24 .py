lista_tareas = []
lista_tareas_ocultas = []

encender = True
while (encender):
    print ("")
    print ("(1) Para Cargar Tareas.")
    print ("(2) Para Mostrar Lista De Tareas.")
    print ("(3) Para Marcar Tareas Como Ocultas.")
    print ("(4) Para Desocultar Tareas.")
    print ("(5) Para Eliminar Una Tarea.")
    print ("(6) Para Salir")
    print ("")
    print ("")

    opcion = raw_input ("Opcion: ")
    print ("")
    if (opcion == "1"):
        while_opcion1 = True
        while (while_opcion1):
            lista_tareas.append(raw_input("Ingrese Tareas, Al Finalizar Escriba (salir1): "))
            for tarea in lista_tareas:
                if (tarea == "salir1"):
                    lista_tareas.remove("salir1")
                    while_opcion1 = False



    elif (opcion == "2"):
        print (lista_tareas)



    elif (opcion == "3"):
        print (lista_tareas)
        print ("")
        while_opcion3 = True

        while (while_opcion3):
            lista_tareas_ocultas.append(raw_input("Ingrese La Tarea Que Quiera Ocultar, Al Finalizar Escriba (salir1): "))
            for tarea_oculta in lista_tareas_ocultas:
                if (tarea_oculta == "salir1"):
                    lista_tareas_ocultas.remove("salir1")
                    while_opcion3 = False
            for tarea in lista_tareas:
                for tarea_oculta in lista_tareas_ocultas:
                    if (tarea == tarea_oculta):
                        lista_tareas.remove(tarea)



    elif (opcion == "4"):
        print (lista_tareas_ocultas)
        print ("")
        while_opcion4 = True

        while (while_opcion4):
            lista_tareas.append(raw_input("Ingrese La Tarea Que Quiera desocultar, Al Finalizar Escriba (salir1): "))
            for tarea in lista_tareas:
                if (tarea == "salir1"):
                    lista_tareas.remove("salir1")
                    while_opcion4 = False
            for tarea_oculta in lista_tareas_ocultas:
                for tarea in lista_tareas:
                    if (tarea_oculta == tarea):
                        lista_tareas_ocultas.remove(tarea_oculta)



    elif (opcion == "5"):
        print (lista_tareas)
        print ("")
        while_opcion5 = True
        while (while_opcion5):
            eliminar = raw_input("Ingrese La Tarea Que Quiera Eliminar, Al Finalizar Escriba (salir1): ")
            if (eliminar == "salir1"):
                while_opcion5 = False
            for tarea in lista_tareas:
                if (tarea == eliminar):
                    lista_tareas.remove(eliminar)



    elif (opcion == "6"):
        encender = False
