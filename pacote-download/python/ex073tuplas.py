times = ('Corintians', 'São Paulo', 'Flamengo', 'Bota fogo', 'Palmeiras', 'Grêmio',
         'Vasco', 'Chapecoense', 'Santos', 'Bahia', 'Cruzeiro')
print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros times são: {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Lista dos times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f"O Chapecoense está na posição {times.index('Chapecoense') + 1 }")
