import os
import math

def verificadorEntrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Digite um valor válido!")

def resolvendoEquacao(num1, num2, num3):
    delta = pow(num2,2) - (4 * num1 * num3)
    sinalB = '+ ' if num2 >= 0 else ''
    sinalC = '+ ' if num3 >= 0 else ''
    if delta > 0:
        x1 = ((-num2) + math.sqrt(delta)) / (2 * num1)
        x2 = ((-num2) - math.sqrt(delta)) / (2 * num1)
        return f"As raízes são reais e distintas,\n {num1}X² {sinalB}{num2}X {sinalC}{num3} => x' = {round(x1,2)} e x'' = {round(x2,2)}"
    elif delta == 0:
        x = (-num2) / (2 * num1)
        return f"A raíz é real e dupla,\n {num1}X² {sinalB}{num2}X {sinalC}{num3} => x' = {round(x,2)}"           
    else:
        xReal = (-num2) / (2 * num1)
        xImaginario = math.sqrt(-delta) / (2 * num1)
        return f"As raízes são complexas,\n {num1}X² {sinalB}{num2}X {sinalC}{num3} => x' = {round(xReal,2)} + {round(xImaginario,2)}i e x'' = {round(xReal,2)} - {round(xImaginario,2)}i"      

def exe():
    print("Olá, bem vindo(a). Esse programa calcula uma equação do segundo grau \n 'ax^2 + bx + c = 0' e determinar as raízes. Pressione qualquer tecla para continuar: ")
    os.system('Pause')
    
    while True:
        num1 = verificadorEntrada("Digite o a: ")
        if num1 == 0:
            print("Essa equação não é de segundo grau, pois o valor 'a' não pode ser 0.")
        else:
            break

    num2 = verificadorEntrada("Digite o b: ")
    num3 = verificadorEntrada("Digite o c: ")
    resultado = resolvendoEquacao(num1, num2, num3)
    print(resultado)
    
exe()
