from random import randint
n = int(input('Qual seu chute? '))
pc = randint (0, 10)
if n == pc:
    print('Parabéns, você acertou de primeira!!!')
    exit()
else:
    tentativas = 2
while n != pc:
    n = int(input('Tente novamente: '))
    if n == pc:
        print(f'Você acertou com {tentativas} tentativas!')
    else:
        tentativas = tentativas + 1