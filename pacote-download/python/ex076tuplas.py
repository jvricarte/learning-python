listagem = ('Lápis', 1.75, 'Borracha', 0.50, 'Caderno', 10, 'Livro', 30.45)
print('-' * 40)
print(f'{"LISTAGEM DE COMPRAS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)