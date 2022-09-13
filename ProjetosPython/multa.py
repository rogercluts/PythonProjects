vel = float(input('Qual foi a velocidade atingida? '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Você será multado(a) e custará {multa}')
else:
    print('Você estava dentro do limite de velocidade!')