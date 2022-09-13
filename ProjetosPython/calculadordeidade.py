from datetime import datetime

ano_nasc = int(input('Em que ano você nasceu?\nR: '))
mes_nasc = int(input('De qual mês?\nR: '))
dia_nasc = int(input('De que dia?\nR: '))

data_nasc = datetime(ano_nasc, mes_nasc, dia_nasc)
data_atual = datetime.now()

diff = data_atual - data_nasc

dias = diff.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30

print(f'Você tem {anos} anos, {meses} meses e {dias} dias de vida.')