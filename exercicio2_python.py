def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def verificarMaioridade(idadeIndividuo):
    if idadeIndividuo >= 18:
        print(f"Maior de idade, você tem {idadeIndividuo}")
    else:
        print(f"Menor de idade, você tem {idadeIndividuo}")

numero = verificadorEntrada("Insira sua idade: ")
verificarMaioridade(numero)