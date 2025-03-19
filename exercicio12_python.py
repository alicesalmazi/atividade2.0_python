import random

escolhasDisponiveis = ['Pedra', 'Papel', 'Tesoura']

def verificadorEscolha():
    while True:
        escolhaUsuario = (input("Escolha 'Pedra', 'Papel' ou 'Tesoura': ")).capitalize().strip()
        if escolhaUsuario in escolhasDisponiveis:
            return escolhaUsuario
            break
        else:
            print("Digite corretamente!")

def partida(escolhaUsuario):
    escolhaComputador = escolhasDisponiveis[random.randint(1,3) - 1]
    ganhouPartida = (escolhaUsuario == escolhasDisponiveis[0] and escolhaComputador == escolhasDisponiveis[2] ) or \
        (escolhaUsuario == escolhasDisponiveis[2] and escolhaComputador == escolhasDisponiveis[1]) or \
            (escolhaUsuario == escolhasDisponiveis[1] == escolhaComputador == escolhasDisponiveis[2])
    
    if ganhouPartida:
        print(f"Parabéns! Você ganhou, {escolhaUsuario} vence {escolhaComputador}.")
    elif escolhaComputador == escolhaUsuario:
        print(f"Empate, ambos escolheram {escolhaUsuario}.")
    else:
        print(f"Você perdeu... {escolhaComputador} vence {escolhaUsuario}.")

escolhaUsuario = verificadorEscolha()
partida(escolhaUsuario)
        