Guardados = {0:0, 1:1}

n = int(input("¿Cuántos numeros de Fibonacci desea saber? \n"))

def Fibonacci(n):
    if n in Guardados:
        return Guardados[n]
    
    Resultado = Fibonacci(n-1) + Fibonacci(n-2)
    Guardados[n] = Resultado
    return Resultado

ListaFibonacci = []

def Imprimir(n):
    for i in range (n + 1):
        ListaFibonacci.append(Guardados[i])
    print(ListaFibonacci)

Fibonacci(n)
Imprimir(n)