def BuscaPrimo():
    Bandera = True
    i = 0
    PrimosCalculados = 0
    Numero = int(input("Ingrese un número entero para saber si es primo o no \n"))
    while Bandera:
        i = i + 1
        Operacion = Numero % i
        if Operacion == 0 and Numero != 0:
            PrimosCalculados += 1
        elif i-1 == Numero and PrimosCalculados > 2:
            print("El número " + str(Numero), "no es primo.")
            Bandera = False
        elif i-1 == Numero and PrimosCalculados == 2:
            print("El número " + str(Numero), "es primo.")
            Bandera = False
        else:
            if Numero <= 1:
                print("Usted ha digitado " + str(Numero), "y no se puede calcular ese valor")
                Bandera = False

BuscaPrimo()