def Triangulos():
    print("Algoritmo para reconocer que tipo de triángulo es según sus lados")
    Lado1 = int(input("Digite el lado 1: "))
    Lado2 = int(input("Digite el lado 2: "))
    Lado3 = int(input("Digite el lado 3: "))
    if (Lado1 + Lado2 > Lado3) and (Lado1 + Lado3 > Lado2) and (Lado2 + Lado3 > Lado1):
        if Lado1 == Lado2 == Lado3:
            print("Es un triángulo equilátero")
        elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
            print("Es un triangulo isóceles")
        else:
            print("Es una triángulo escaleno")
    else:
        print("La suma de dos de sus lados no es mayor que el tercero, no se puede clasificar")

Triangulos()
