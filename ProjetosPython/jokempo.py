from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
nome = input('Olá, qual é o seu nome? ')
inicio = int(input(f'Vamos jogar JoKenPô, {nome}? \n 1) SIM \n 2) NÃO\n R: '))
sim = 1
nao = 2
if inicio == 1:
    jogador = int(input('Suas opções:\n 0 = Pedra\n 1 = Papel\n 2 = Tesoura\n Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    sleep(0.7)
    print('-=' * 11)
    print(f'Computador jogou: {itens[computador]}')
    print(f'Jogador jogou: {itens[jogador]}')
    print('-=' * 11)
    if computador == 0:
        if jogador == 0:
            print('\033[1:34mEMPATE')
        elif jogador == 1:
            print('\033[1:32mJOGADOR VENCE')
        elif jogador == 2:
            print('\033[1:31mCOMPUTADOR VENCE')
        else:
            print('JOGADA INVALIDA')
    elif computador == 1:
        if jogador == 0:
            print('\033[1:31mCOMPUTADOR VENCE')
        elif jogador == 1:
            print('\033[1:34mEMPATE')
        elif jogador == 2:
            print('\033[1:32mJOGADOR VENCE')
        else:
            print('JOGADA INVALIDA')
    elif computador == 2:
        if jogador == 0:
            print('\033[1:32mJOGADOR VENCE')
        elif jogador == 1:
            print('\033[31mCOMPUTADOR VENCE')
        elif jogador == 2:
            print('\033[1:34mEMPATE')
        else:
            print('\033[1:33mJOGADA INVALIDA')
elif inicio == 2:
    print(f'Ok {nome}... Obrigado pela atenção.')
