def Password():
    Correcta = False
    while not Correcta:
        Ingreso = input("Ingrese la contraseña de usuario\n")
        if Ingreso == "admin123":
            print("Acceso consedido \n" \
            "Bienvenido Admin")
            Correcta = True
        else:
            print("La contraseña es incorrecta")

Password()