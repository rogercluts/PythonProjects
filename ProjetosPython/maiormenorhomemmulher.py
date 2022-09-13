somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0
for p in range (1, 5):
    print(f'----- {p}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadeh} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')