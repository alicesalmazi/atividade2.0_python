def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Digite um valor válido!")

def verificarNumero(numero):
    if 10 >= numero <= 20:
        print(f"Número {numero} entre 10 e 20.")
    else:
        print(f"Número {numero} fora do intervalo.")

numero = verificadorEntrada("Digite um número: ")
verificarNumero(numero)
