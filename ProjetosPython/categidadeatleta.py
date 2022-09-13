from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
a = date.today().year - ano
if a <= 9:
    print('Você está na categoria MIRIM!')
elif a <= 14:
    print('Você está na categoria INFANTIL!')
elif a <= 19:
    print('Você está na categoria SÊNIOR!')
elif a > 19:
    print('Você está na categoria MASTER!')