casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anospag = int(input('Em quantos anos você vai pagar o imóvel? '))
prest = casa / (anospag * 12)
if prest > (30/100)*salario:
    print('O empréstimo foi negado...')
else:
    print(f'Meus parabéns pela sua nova aquisição, a parcela será de R${prest:.2f}')