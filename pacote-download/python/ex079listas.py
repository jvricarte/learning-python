num = list()
res = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
    else:
        print('Número duplicado, não vou adicionar')
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if res in 'Nn':
        break
print('-' * 30)
num.sort()
print(f'Você digitou os números {num}')
