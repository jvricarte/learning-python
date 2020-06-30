while True:
    n = int(input('''Digite um número positivo para ver a sua tabuada
ou um negativo para sair do programa: '''))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('TABUADA ENCERRADA')
