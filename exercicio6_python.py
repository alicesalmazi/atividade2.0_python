def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def soma(num1, num2):
    if num1 + num2 > 100:
         print("Soma maior que 100.")
    else:
         print("Soma menor ou igual a 100.")

num1 = verificadorEntrada("Insira o 1° valor: ")
num2 = verificadorEntrada("Insira o 2° valor: ")

soma(num1, num2)