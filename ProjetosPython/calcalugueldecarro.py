km = float(input('Quantos km foram percorridos pelo carro alugado?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
pago = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${pago:.2f}')