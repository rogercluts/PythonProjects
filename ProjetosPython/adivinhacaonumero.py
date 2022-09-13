from random import randint
pc = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número de 0 a 10.\nTente adivinhar!')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez')
        elif jogador > pc:
            print('Menos... Tente mais uma vez')
print(f'Você acertou com {tentativas} tentativas!')