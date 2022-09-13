times = ('Palmeiras', 'Corinthians', 'Atlético-PR', 'Internacional', 
        'Atletico-MG', 'Fluminense', 'Santos', 'São Paulo', 
        'Flamengo', 'Botafogo', 'Avaí', 'Bragantino', 'Atlético-GO', 
        'Goiás', 'Ceará SC', 'Coritiba', 'América-MG', 
        'Cuiabá', 'Juventude', 'Fortaleza')

print('-=' * 20)
print(f'Lista de times: {times}')
print('-=' * 20)
print(f'Os cinco primeiros são: {times[0:5]}')
print('-=' * 20)
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabpetica: {sorted(times)}')
print('-=' * 20)
print(f'O São Paulo está na {times.index("São Paulo") + 1}º posição')