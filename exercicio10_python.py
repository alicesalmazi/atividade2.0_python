def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Digite um valor raro!")

def verificadorMaiorMenor(num1,num2,num3):
    if num1 < num2 > num3:
        print(f"Dos três números inseridos {num2} é o maior")
    elif num2 < num1 > num3:
        print(f"Dos três números inseridos {num1} é o maior")
    else:
        print(f"Dos três números inseridos {num3} é o maior")

num1 = verificadorEntrada("Digite o 1° número: ")
num2 = verificadorEntrada("Digite o 2° número: ")
num3 = verificadorEntrada("Digite o 3° número: ")
verificadorMaiorMenor(num1, num2, num3)