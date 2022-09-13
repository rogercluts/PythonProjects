from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}, Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('JOGADOR VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('VAMOS JOGAR NOVAMENTE...')
print(f'GAME OVER. Você venceu {v} vezes.')