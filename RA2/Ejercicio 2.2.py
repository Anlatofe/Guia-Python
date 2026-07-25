def SumaPromedio():
    ListaAcumulacion = []
    Numero = 0
    Acumulacion = 0
    SumaNegativos = 0
    SumaPositivos = 0
    Neutros = 0
    Sumatoria = 0
    while Numero != -1:
        Numero = int(input("Ingrese números enteros, para salir del bucle digite -1 \n"))
        print("Usted ingresó el " + str(Numero))
        ListaAcumulacion.append(Numero)
    print("Los números ingresados son los siguientes:")
    print(ListaAcumulacion)
    for Lista in ListaAcumulacion:
        Acumulacion = Acumulacion + Lista
        if Lista < 0:
            SumaNegativos += 1
            Sumatoria += 1
        elif Lista == 0:
            Neutros += 1
            Sumatoria += 1
        else:
            SumaPositivos += 1
            Sumatoria += 1
    Promedio = Acumulacion / Sumatoria
    print("La suma total de los valores introducidos es "+ str(Acumulacion), ", \n la cantidad de valores negativos fue " \
    "de " + str(SumaNegativos), " \n de positivos fue de "+ str(SumaNegativos), "\n de neutros fue de " + str(Neutros), \
    "\n para un promedio de " + str(Promedio))

SumaPromedio()