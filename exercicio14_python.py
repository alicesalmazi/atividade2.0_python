def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor in [0, 1]:
                return valor
            else:
                print("Digite 1 ou 0")
        except ValueError:
            print("Digite um valor válido!")


def calcularNumero(bit1,bit2,bit3,bit4,bit5):
    byts = f"{bit1}{bit2}{bit3}{bit4}{bit5}"
    
    decimal = (int(byts[0]) * pow(2,4)) + \
            (int(byts[1]) * pow(2,3)) + \
            (int(byts[2]) * pow(2,2)) + \
            (int(byts[3]) * pow(2,1)) + \
            (int(byts[4]) * pow(2,0))
    print(f"{byts} equivale ao número {decimal}")

bit1 = verificadorEntrada("Digite o bit 1 (0 ou 1): ")
bit2 = verificadorEntrada("Digite o bit 1 (0 ou 1): ")
bit3 = verificadorEntrada("Digite o bit 1 (0 ou 1): ")
bit4 = verificadorEntrada("Digite o bit 1 (0 ou 1): ")
bit5 = verificadorEntrada("Digite o bit 1 (0 ou 1): ")
calcularNumero(bit1,bit2,bit3,bit4,bit5)
