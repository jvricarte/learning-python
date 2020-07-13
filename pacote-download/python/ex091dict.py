from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(0, 9),
       'jogador2': randint(0, 9),
       'jogador3': randint(0, 9),
       'jogador4': randint(0, 9)}
ranking = []
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('-=' * 20)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
