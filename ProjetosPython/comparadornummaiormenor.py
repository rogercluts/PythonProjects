n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O {n2} é maior que {n1}')
else:
    print('NÃO EXISTE valor maior, os dois são iguais.')