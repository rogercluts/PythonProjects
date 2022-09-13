from random import randrange
print('Vou pensar em um número entre 0 e 4. Tente adivinhar: ')
a = randrange(0, 4)
b = int(input('Em que número eu pensei? '))
if b == a:
    print('PROCESSANDO...')
    print(f'Você ACERTOU!!! Eu pensei em {a} e você também!! :)')
else:
    print('PROCESSANDO...')
    print(f'Eu pensei em {a} e não em {b}')