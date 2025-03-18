def verificador(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def classificandoNumero(numeroEscolhido):
    if numeroEscolhido == 0:
        print(0)
    elif numeroEscolhido % 2 == 0:
        print(f"O número {numeroEscolhido} é par.")
    else:
        print(f"O número {numeroEscolhido} é impar.")

numero = verificador("Insira um número: ")
classificandoNumero(numero)

    
