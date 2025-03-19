def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Digite um valor válido!")

def calcularPisos(larguraSala, comprimentoSala, larguraPiso, tamanhoPiso):
    areaSala = larguraSala * comprimentoSala
    areaPiso = larguraPiso * tamanhoPiso
    qntPisos = areaSala / areaPiso
    print(f"A quantidade de pisos utilizados será {int(qntPisos)}")



larguraSala = verificadorEntrada("Digite a largura da sala: ")
comprimentoSala = verificadorEntrada("Digite o comprimento da sala: ")
larguraPiso = verificadorEntrada("Digite a largura do piso: ")
tamanhoPiso = verificadorEntrada("Digite o tamanho do piso: ")
calcularPisos(larguraSala, comprimentoSala, larguraPiso, tamanhoPiso)

