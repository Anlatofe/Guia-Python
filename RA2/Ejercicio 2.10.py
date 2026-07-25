def Binario(Numero):
    if Numero == 0:
        return "Ingresaste 0"
        
    ConversionBinario = ""
    while Numero > 0:
        residuo = Numero % 2
        ConversionBinario = str(residuo) + ConversionBinario
        Numero = Numero // 2
        
    return ConversionBinario


Numero = int(input("Ingrese un número decimal: \n"))
print(Binario(Numero))