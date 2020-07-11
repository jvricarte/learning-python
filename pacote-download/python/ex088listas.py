from random import randint
from time import sleep
lista = list()
jogos = list()
tot = 1
print('-' * 20)
print('     MEGA SENA     ')
print('-' * 20)
quant = int(input('Quantidade de jogos que deseja fazer: '))
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        if len(lista) == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} jogos', '-=' * 3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')
