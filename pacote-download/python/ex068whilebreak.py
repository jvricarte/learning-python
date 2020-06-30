from random import randint
v = 0
print('-' * 30)
print('JOGO DO PAR OU IMPAR')
print('-' * 30)
while True:
    jogador = int(input('Digite um número: '))
    comp = randint(0, 11)
    total = jogador + comp
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {comp}, o total é {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
