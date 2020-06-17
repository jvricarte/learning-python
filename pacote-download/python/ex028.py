from random import randint
from time import sleep
comp = randint (0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jog = int(input('Em que número estou pensando? '))
print('PROCESSANDO...')
sleep(3)
if jog == comp:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Eu estava pensando no número {} e não no {}'. format(comp, jog))
