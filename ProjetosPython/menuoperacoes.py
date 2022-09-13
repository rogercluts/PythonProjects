n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
menu = 0
while menu != 4:
    menu = int(input('[0]SOMAR\n[1]MULTIPLICAR\n[2]SABER O MAIOR\n[3]DIGITAR NOVOS NÚMEROS\n[4]SAIR DO PROGRAMA\nO que você deseja fazer? '))
    if menu == 0:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} equivale a {soma}')
    elif menu == 1:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} equivale a {mult}')
    elif menu == 2:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif menu == 3:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif menu == 4:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente. ')
    print('=-=' * 10)
print('Fim do programa, volte sempre!')