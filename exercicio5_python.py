def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def classificacaoTriangulo(lado1,lado2,lado3):
    area = (lado1 * lado2) / 2
    if lado1 == lado2 == lado3:
        print(f"Triângulo Equilátero de área {area}.")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print(f"Triângulo Isósceles de área {area}.")
    else:
        print(f"Triângulo Escaleno de área {area}.")

lado1 = verificadorEntrada("Insira o valor do lado 1: ")
lado2 = verificadorEntrada("Insira o valor do lado 2: ")
lado3 = verificadorEntrada("Insira o valor do lado 3: ")

classificacaoTriangulo(lado1,lado2,lado3)
