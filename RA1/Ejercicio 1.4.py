import math


def Figuras():
    while True:
        print("\n1. Área de un círculo")
        print("2. Área de un rectángulo")
        print("3. Área de un triángulo")
        print("4. Perímetro de un cuadrado")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()
        if opcion not in ["1", "2", "3", "4"]:
            print("\nPor favor, digite un número del 1 al 5.")
            continue
        try:
            if opcion == "1":
                radio = float(input("Ingrese el radio del círculo: "))
                if radio <= 0:
                    print("El radio debe ser un número mayor a cero.")
                else:
                    area = math.pi * (radio ** 2)
                    print("El área del círculo es: ", area)
            elif opcion == "2":
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                if base <= 0 or altura <= 0:
                    print("Error: Las dimensiones deben ser números mayores a cero.")
                else:
                    area = base * altura
                    print("El área del rectángulo es: ", area)
            elif opcion == "3":
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                if base <= 0 or altura <= 0:
                    print("Error: Las dimensiones deben ser números mayores a cero.")
                else:
                    area = (base * altura) / 2
                    print("El área del triángulo es: ", area)
            elif opcion == "4":
                lado = float(input("Ingrese el lado del cuadrado: "))
                if lado <= 0:
                    print("Error: El lado debe ser un número mayor a cero.")
                else:
                    perimetro = lado * 4
                    print("El perímetro del cuadrado es: ", perimetro)
            if opcion == "5":
                print("Menú cerrado.")
                break
        except ValueError:
            print("Inválido. Ingrese solo números.")

Figuras()