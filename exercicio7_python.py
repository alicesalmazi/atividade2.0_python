def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def verificadorMes():
    while True:
        mes = verificadorEntrada("Insira um número de 1 a 12: ")
        if 1 <= mes <= 12:
            mesesDoAno = ["Janeiro", "Fevereiro", "Março", "Abril", 
                          "Maio", "Junho", "Julho", "Agosto", 
                          "Setembro", "Outubro", "Novembro", "Dezembro"]
            mesEscolhido = mesesDoAno[mes - 1]
            print(f"O mês escolhido é: {mesEscolhido}")
            break 
        else:
            print("Número inválido. Por favor, insira um número entre 1 e 12.")

verificadorMes()