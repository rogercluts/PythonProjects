print()
print('=================================================')
print('         Bem-vindo ao Jogo da Cobrinha!          ')
print('=================================================')
print()

nlinhas = int(input('Número de linhas do tabuleiro : '))
ncols   = int(input('Número de colunas do tabuleiro: '))
x0      = int(input('Posição x inicial da cobrinha : '))
y0      = int(input('posição y inicial da cobrinha : '))
t       = int(input('Tamanho da cobrinha           : '))
if x0 - (t - 1) < 0:
    print()
    print("A COBRINHA NÃO PODE FICAR NA POSIÇÃO INICIAL INDICADA")

else:
    d = 0
    i = 1
    while i <= t-1:
        d = d * 10 + 2
        i = i + 1
    
    direcao = 1
    
    while direcao != 5:
        imprime_tabuleiro(nlinhas, ncols, x0, y0, d)
        print("1 - esquerda | 2 - direita | 3 - cima | 4 - baixo | 5 - sair do jogo")
        direcao = int(input("Digite o número do seu próximo movimento: "))

        if direcao != 5:
            x0, y0, d = move(nlinhas, ncols, x0, y0, d, direcao)

print()        
print("Tchau!")

def num_digitos(n):
    n = int(input('qual é o numero: ')) 
    num_digitos = 0
    i = 0
    while n != 0:
        i = n % 10
        n = n // 10 
        num_digitos = num_digitos + 1
        i = i + 1

    print("Número de digitos é", num_digitos)

    return num_digitos

def pos_ocupada(nlinhas, ncols, x, y, x0, y0, d):
    Achei = False

    while (d != 0):
        resto = d % 10
        d = d // 10

        if resto == 1:
            x0 = x0 + 1

        if resto == 2:
            x0 = x0 - 1

        if resto == 3:
            y0 = y0 - 1

        if resto == 4:
            y0 = y0 + 1

        if x == x0 and y == y0:
            achei = True

    return True

def imprime_tabuleiro(nlinhas, ncols, x0, y0, d):
    print("Vixe! Ainda não fiz a função imprime_tabuleiro()!")

def move(nlinhas, ncols, x0, y0, d, direcao):
    print("Vixe! Ainda não fiz a função move()!")

    return x0, y0, d

main()   