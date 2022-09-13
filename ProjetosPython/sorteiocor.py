from random import choice
n1 = input('Primeira cor: ')
n2 = input('Segunda cor: ')
n3 = input('Terceira cor: ')
lista = [n1, n2, n3]
escolhido = choice(lista)
print(f'A cor escolhida foi {escolhido}')

