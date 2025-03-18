def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def verificadorParImpar(numero):
    if numero % 2 == 0:
        print(f"{numero} é um número par!")
    else:
        print(f"{numero} é um número impar!")

resposta = verificadorEntrada("Insira um valor aleatório: ")
verificadorParImpar(resposta)