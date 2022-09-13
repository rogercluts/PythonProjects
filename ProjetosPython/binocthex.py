n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n 1) BINÁRIO\n 2)OCTAL\n 3)HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{n} convertido para binario é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção invalida, tente novamente.')
