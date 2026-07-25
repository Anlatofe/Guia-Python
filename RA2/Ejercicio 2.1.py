def Multiplicacion():
    Numero = int(input("Digite un número para saber su tabla de multiplicación del 1 al 12 \n"))
    for i in range(1, 12):
        Resultado = Numero * i
        print(str(Numero) + " x " + str(i), " = " + str(Resultado))

Multiplicacion()