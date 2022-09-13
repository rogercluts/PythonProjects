nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2)/2

if media < 5:
    print('Você foi... REPROVADO.')
elif media >= 5 and media < 6.9:
    print('Você está de RECUPERAÇÃO.')
elif media >= 7:
    print('Você foi... APROVADO!! :)')