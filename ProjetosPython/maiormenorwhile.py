n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
menu = int(input(' [0] SOMAR\n [1] MULTIPLICAR\n [2] MAIOR\n [3] NOVOS NÚMEROS\n [4] SAIR DO PROGRAMA\n O que você deseja? '))
maior = 0
menor = 0
if n1 > n2:
    maior = n1
else:
    maior = n2
while menu == 0:
    print(n1+n2)
    menu = menu + 9
else:
    if menu == 1:
        print(n1 * n2)
    if menu == 2:
        print(f'Entre {n1} e {n2}, o maior é {maior}')
    if menu == 3:
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro novo número: '))
        menu = int(input(
            ' [0] SOMAR\n [1] MULTIPLICAR\n [2] MAIOR\n [3] NOVOS NÚMEROS\n [4] SAIR DO PROGRAMA\n O que você deseja? '))
    if menu == 4:
        print('FIM')

