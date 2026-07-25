import random as rd

def AdivinarNumero():
    NumeroRandom = rd.randint(1,100)
    Bandera = True
    i = 1
    print("Adivina el número entre el 1 y el 100")
    while Bandera:
        NumeroEscrito = int(input("Digite un número: "))
        if NumeroEscrito == NumeroRandom:
            print("Felicidades, has adivinado el número en ", i, " intentos")
            Bandera = False
        elif NumeroEscrito > NumeroRandom:
            print("El número es menor")
        else:
            print("El número es mayor")
        i += 1

AdivinarNumero()