Numeros = 0
Bandera = True

def Sumar(Numeros):
    elementos = Numeros.replace(" ", "").split("+")
    resultado = float(elementos[0])
    for elemento in elementos[1:]:
        resultado += float(elemento)
    return resultado

def Restar(Numeros):
    elementos = Numeros.replace(" ", "").split("-")
    resultado = float(elementos[0])
    for elemento in elementos[1:]:
        resultado -= float(elemento)
    return resultado

def Multiplicar(Numeros):
    elementos = Numeros.replace(" ", "").split("*")
    resultado = float(elementos[0])
    for elemento in elementos[1:]:
        resultado *= float(elemento)
    return resultado

def Dividir(Numeros):
    elementos = Numeros.replace(" ", "").split("/")
    resultado = float(elementos[0])
    for elemento in elementos[1:]:
        Valor = float(elemento)
        if Valor == 0:
            return("No dividas entre cero, no se puede")
        resultado /= float(elemento)
    return resultado

def Potencia(Numeros):
    elementos = Numeros.replace(" ", "").split("**")
    resultado = float(elementos[0])
    for elemento in elementos[1:]:
        resultado **= float(elemento)
    return resultado



while Bandera:
    Opcion = int(input("Bienvenido al menú de opciones ¿cual opción va a elegir para su necesidad?  "))
    if Opcion == 1:
        Numeros = input("¿Cuales números va a sumar? (Use . para los decimales y use el signo +) ")
        print(Sumar(Numeros))
    elif Opcion == 2:
        Numeros = input("¿Cuales números va a restar? (Use . para los decimales y use el signo -) ")
        print(Restar(Numeros))
    elif Opcion  == 3:
        Numeros = input("¿Cuales números va a multiplicar? (Use . para los decimales y use el signo *) ")
        print(Multiplicar(Numeros))
    elif Opcion == 4:
        Numeros = input("¿Cuales números va a dividir? (Use el signo /) ")
        print(Dividir(Numeros))
    elif Opcion == 5:
        Numeros = input("¿Cuales números va a potenciar? (Use **) ")
        print(Potencia(Numeros))
    elif Opcion == 6:
        print("Salida")
        Bandera = False
    else:
        print("Opción invalida, elija una de las opciones existentes")
