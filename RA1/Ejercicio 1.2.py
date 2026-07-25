SalarioBase = 15000
Horas = 0

def Salariado():
    print("Calculadora de salario. Cuando complete 40 horas su salario pago por hora será del 150%")
    Horas = int(input("¿Cuantas horas trabajó? "))
    if Horas > 40:
        print("Como ha cumplido 40 horas, su pago incrementa al 150%")
        Pago40Horas = SalarioBase * 40
        HorasExtra = Horas - 40
        SalarioExtra = HorasExtra * (SalarioBase * 1.5)
        PagoBruto = int(SalarioExtra + Pago40Horas)
        print("Su salario es de " + str(PagoBruto))
        if PagoBruto > 1500000:
            Descuento = int(PagoBruto * 0.04)
            PagoNeto = PagoBruto - Descuento
            print("El descuento es de " + str(Descuento))
            print("Su salario después de aplicado el descuento del 4% en salud es de " + str(PagoNeto))
    else:
        print("No ha cumplido 40 horas de trabajo")
        PagoNeto = SalarioBase * Horas
        print("Su salario final es de " + str(PagoNeto))

Salariado()