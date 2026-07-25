Distancia = float(input("Digite una distancia, tenga en cuenta que será en unidad de kilómetros. Se admiten decimales. "))
Metros = 0

def AMetro(Distancia):
    print("Se realizará la conversión a metros.")
    Metros = Distancia * 1000
    print("La conversión de " + str(Distancia) + " kilometro(s) a metros da como resultado " + str(Metros) + " metros.")

def ACentimetro(Metros):
    print("Se hará la conversión a unidades de centímetro")
    Centimetros = Metros * 100
    print("La conversión a centímetros dió como resultado " + str(Centimetros) + " cm.")

def AMilla(Distancia):
    print("Se convertirá la unidad de kilómetros a millas")
    Millas = Distancia * 0.621371
    print(str(Distancia) + " kilómetro(s) equivalen a " + str(Millas) + " millas.")


AMetro(Distancia)
ACentimetro(Metros)
AMilla(Distancia)
