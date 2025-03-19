from datetime import datetime, date

def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor > datetime.today().year:
                print(f"Ano de nascimento não pode ser maior que {datetime.today().year}.")
            elif valor < 1900:
                print("Digite um ano maior que 1900!")
            else:
                return valor
        except ValueError:
            print("Digite um valor válido!")

def classificacaoIdade(anoNascimento):
    dataAtual = datetime.today().year
    idade = dataAtual - anoNascimento
    if idade < 12:
        print(f"{idade} = Criança.")
    elif idade < 18:
        print(f"{idade} = Adolescente.")
    elif idade < 36:
        print(f"{idade} = Adulto Jovem.")
    else:
        print(f"{idade} = Adulto.")

anoNascimento = verificadorEntrada("Digite seu ano de nascimento: ")
classificacaoIdade(anoNascimento)