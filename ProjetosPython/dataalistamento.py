from datetime import date
nascimento = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year - nascimento
falta = 18 - ano
passou = ano - 18
if ano < 18:
    print('Você ainda terá que se alistar.')
    print(f'Faltam {falta} anos')
elif ano == 18:
    print('ESTA NA HORA DE SE ALISTAR!!')
elif ano > 18:
    print('Já passou o periodo de alistamento...')
    print(f'Se passaram {passou} anos')
