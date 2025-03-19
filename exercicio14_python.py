def verificadorEntrada(mensagem):
    while True:
        byts = input(mensagem)
        if len(byts) == 5 and all(n in ['0','1'] for n in byts):
            return byts
        else:
            print("Digite um valor válido!")


def calcularNumero(byts):
    decimal = (int(byts[0]) * pow(2,4)) + \
            (int(byts[1]) * pow(2,3)) + \
            (int(byts[2]) * pow(2,2)) + \
            (int(byts[3]) * pow(2,1)) + \
            (int(byts[4]) * pow(2,0))
    print(f"{byts} equivale ao número {decimal}")

byts = verificadorEntrada("Digite um número binário com 5 caracteres: ")
calcularNumero(byts)

