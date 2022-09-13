salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    aumentosalario = salario + (salario * 15 / 100)
else:
    aumentosalario = salario + (salario * 10 / 100)
print(f'Quem ganhava {salario:.2f} passa a ganhar {aumentosalario:.2f}')