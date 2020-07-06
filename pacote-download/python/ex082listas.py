lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar? [S/N]: ')).strip()
    if res in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
