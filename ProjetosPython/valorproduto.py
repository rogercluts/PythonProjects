preco = float(input('Qual é o valor do produto? '))
condpag = int(input('Qual é o metodo de pagamento?\n 1)À vista no dinheiro (10% de desconto)\n 2)À vista no cartão (5% de desconto)\n 3)Em até 2x no cartão (preço normal)\n 4)3x ou mais no cartão (20% de JUROS)\n Método escolhido: '))
if condpag == 1:
    vd = preco - ((10 / 100) * preco)
    print(f'Ficará {vd} reais')
elif condpag == 2:
    vc = preco - ((5 / 100) * preco)
    print(f'Ficará {vc} reais')
elif condpag == 3:
    parcela = preco / 2
    print(f'Ficará 2 parcelas de {parcela} reais, saindo no total: {preco} reais sem juros')
elif condpag == 4:
    total = preco + (preco * 20/100)
    tempo = float(input('Em quantas vezes deseja parcelar? '))
    tvc = total / tempo
    print(f'Sua compra de {preco:.2f} será parcelada em {tempo:.2f}x de {total:.2f}')
else:
    total = 0
    print('Opção invalida de pagamento. TENTE NOVAMENTE!')