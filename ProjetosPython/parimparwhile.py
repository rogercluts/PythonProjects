from random import randint
soma_vit = 0
print('=-=' * 25)
print('*' * 12, 'VAMOS JOGAR PAR OU IMPAR', '*' * 12)
while True:
    print('=-=' *25)
    num_pc = randint(0, 10)
    parimpar_human = str(input('Digite \033[1;33m[P]\033[m para Par ou \033[1;36m[I]\033[m para Impar.')).strip().upper()[0]
    if parimpar_human == 'P':
        parimpar_pc = 'I'
    if parimpar_human in 'ÍíiI':
        parimpar_human = 'Í'
        parimpar_pc = 'P'
    num_human = int(input('Digite um número: '))
    soma_num = num_pc + num_human
    resp = ''

    if soma_num % 2 == 0:
        resp = 'Par'
    elif soma_num % 2 == 1:
        resp = 'Ímpar'

    if parimpar_human == resp[0]:
        soma_vit += 1
        print('Parabéns, você \033[1;34mVENCEU!\033[m')
        print(f'O computador jogou {num_pc} e você {num_human}. Total {soma_num} que é {resp}')
    elif parimpar_pc == resp[0]:
        print('Que pena, você \033[1;35mPERDEU...\033[m')
        print(f'O computador jogou {num_pc} e você {num_human}. Total {soma_num} que é {resp}')
        print('=-=' * 20)
        break
    print('=-=' * 50)
    print(f'Fim de jogo. Você venceu durante {soma_vit} vezes seguidas!')