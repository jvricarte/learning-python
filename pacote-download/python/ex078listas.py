listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] < menor:
            menor = listanum[c]
        if listanum[c] > maior:
            maior = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor é o {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...')
print(f'O menor valor lido é o {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
