def verificadorEntrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor == valor:
                return valor
        except ValueError:
            print("Insira um valor válido.")

def verificarAno(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print("é")
    else:
        print("não é")

#import calendar
#def verificadorAno():
    #if calendar.isleap(ano):
    #   print("é")
    #else:
    #   print("não é")

ano = verificadorEntrada("Insira um ano: ")
verificarAno(ano)