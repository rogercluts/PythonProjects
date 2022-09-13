dist = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a coemçar uma viagem de {dist}KM')
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print(f'Nessa viagem você gastará {preco:.2f} reais')