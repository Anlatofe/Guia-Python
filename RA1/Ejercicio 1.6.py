def Calificacion():
    ListaNotas = []
    NotaAcumulada = 0
    print("Este programa se usará para calcular el promedio de las notas de los estudiantes. Se admiten solo 5 notas de 0 a 100")
    for i in range (0, 5):
        NotaALista = int(input(f"Ingrese la nota número {i+1} : "))
        NotaAcumulada += NotaALista
        ListaNotas.append(NotaALista)
    if NotaAcumulada / i < 60:
        print(f"El promedio del estudiante es de {NotaAcumulada/i:.2f} por lo tanto ha reprobado.")
    else:
        print(f"El promedio del estudiante ha sido de {NotaAcumulada/i:.2f} por lo que representa una aprobación.")
    maximo = ListaNotas[0]
    minimo = ListaNotas[0]
    for Nota in ListaNotas:
        if Nota > maximo:
            maximo = Nota
        if Nota < minimo:
            minimo = Nota
    print(f"La nota máxima del estudiante ha sido de {maximo} y la mínima de {minimo}.")

Calificacion()