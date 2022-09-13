while True:
    n = int(input('Digite o número para saber a tabuada: '))
    if n < 0:
        break
    print(f'Tabuada do {n}')
    for c in range (1, 11):
        print(f'{n}x{c}={n*c}')
print(f'Não foi possível encontrar a tabuada de {n}, tente novamente')