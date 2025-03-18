def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

num1 = verificadorEntrada("Insira um valor aleatório: ")
num2 = verificadorEntrada("Insira um valor aleatório: ")

def verificadorValor(num1, num2):
    if num1 == num2:
        print(f"Números iguais! {num1} = {num2}.")
    else: 
        print(f"Números diferentes! {num1} ≠ {num2}")

verificadorValor(num1,num2)    