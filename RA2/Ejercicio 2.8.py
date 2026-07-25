n = int(input("Ingrese el número de filas para hacer el triángulo: "))

for fila in range(1, n + 1):
    for columna in range(1, fila + 1):
        print("*", end="")
        
    print()
