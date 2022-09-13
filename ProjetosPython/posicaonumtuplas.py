num = (int(input('Digite um valor: ')), 
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')), 
        int(input('Digite o último valor: ')))

print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')