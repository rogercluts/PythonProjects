peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
calcIMC = (peso / altura ** 2)

if calcIMC < 18.5:
    print(f'Você está abaixo do peso, seu IMC é de {calcIMC:.1f}')
elif calcIMC >= 18.5 and calcIMC <= 25:
    print(f'Você está no peso ideal, seu IMC é de {calcIMC:.1f}')
elif calcIMC >= 25 and calcIMC <= 30:
    print(f'Você está acima do seu peso ideal, seu IMC é de {calcIMC:.1f}')
elif calcIMC > 30 and calcIMC <= 40:
    print(f'Você está em estado de obesidade, seu IMC é de {calcIMC:.1f}')
elif calcIMC > 40:
    print(f'Seu caso é de OBESIDADE MORBIDA (procure um médico), seu IMC é de {calcIMC}')
