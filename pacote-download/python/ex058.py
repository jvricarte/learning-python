from random import randint
from time import sleep
tent = 1
comp = randint(0, 10)
print('=-' * 10)
print('JOGO DE ADIVINHAÇÃO')
print('=-' * 10)
print('Estou pensando em um número entre 0 e 10...')
print('Você consegue adivinhar qual é?')
jog = int(input('Qual é o seu palpite? '))
print('Hum...')
sleep (1)
while jog != comp:
    tent = tent + 1
    if jog > comp:
        jog = int(input('Estou pensando em um número menor... '))
    else:
        if jog < comp:
            jog = int(input('Estou pensando em um número maior... '))
print('PARABÉNS! Você acertou!!!')
print('Você precisou de {} tentativas'.format(tent))
